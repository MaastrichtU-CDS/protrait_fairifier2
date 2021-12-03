from datetime import timedelta, datetime
from pathlib import Path
import os
import logging
import requests

from airflow import DAG
from airflow.utils.decorators import apply_defaults
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

import rdflib as rdf
from SPARQLWrapper import SPARQLWrapper, POSTDIRECTLY


def upload_triples_dir(input_path, sparql_endpoint, empty_db=True, **kwargs):
    """Uploads all .nt files in a directory to the given sparql endpoint. 
    All files will be assigned to a graph based on the filename of the triples file.

    Args:
        input_path (pathlib.Path): The location for the triples files
        sparql_endpoint (str): The sparql endpoint (without /statements at the end)
        empty_db (bool, optional): Indicates whether the db should be emptied before inserting. Defaults to True.
    """   
    LOGGER = logging.getLogger("airflow.task")
    LOGGER.info(f'uploading dir {str(input_path)} to {sparql_endpoint}')

    sparql = SPARQLWrapper(sparql_endpoint + '/statements')

    if empty_db:
        LOGGER.info("Dropping all existing graphs")
        deleteQuery = """
                DROP NAMED
            """

        sparql.setQuery(deleteQuery)
        sparql.query()

    for file in input_path.glob('*.nt'):
        upload_triples_file(file, sparql_endpoint, empty_db=False)

def upload_terminology(url, sparql_endpoint, **kwargs):
    """Uploads a given ontology file to the SPARQL endpoint
    
    """
    LOGGER = logging.getLogger("airflow.task")
    LOGGER.info(f'downloading file {url}')

    ret = requests.get(url)

    LOGGER.debug(f'got return code {ret.status_code}')

    if ret.status_code >= 200 and ret.status_code < 300:
        sparql = SPARQLWrapper(sparql_endpoint)

        LOGGER.info(f'starting upload to {sparql_endpoint}')
        g = rdf.Graph()
        g.parse(data=ret.text)
        triples = g.serialize(format='nt')

        for i in range(0, len(triples), 100000):
            LOGGER.info(f'uploading {100000 if i + 100000 < len(triples) else len(triples) % 100000} triples')

            query = """
            INSERT DATA {
                GRAPH <http://localhost/ontology> {
                    %s
                } 
            }
            """ % ('\n'.join(triples[i:(i + 100000 if (i+100000) < len(triples) else len(triples))]))

            sparql.setRequestMethod(POSTDIRECTLY)
            sparql.setQuery(query)
            sparql.query()
        
def upload_triples_file(filename, sparql_endpoint, empty_db=True, **kwargs):
    """Uploads a single triples (.nt) file to a given sparql endpoint.

    Args:
        filename (pathlib.Path): The input file
        sparql_endpoint (str): The sparql endpoint (without /statements at the end) 
        empty_db (bool, optional): Indicates whether the db should be emptied before inserting. Defaults to True.
    """    
    LOGGER = logging.getLogger("airflow.task")
    LOGGER.info(f'uploading file {str(filename)} to {sparql_endpoint}')


    sparql = SPARQLWrapper(sparql_endpoint + '/statements')

    if empty_db:
        LOGGER.info("Dropping all existing graphs")
        deleteQuery = """
                DROP NAMED
            """

        sparql.setQuery(deleteQuery)
        sparql.query()

    with open(filename, 'r') as f:
        filedata = f.readlines()
        LOGGER.info(f'Found {len(filedata)} lines (triples) in file {str(filename)}')


    for i in range(0, len(filedata), 100000):
        g = rdf.Graph()
        g.parse(
            data='\n'.join(filedata[i:(i + 100000 if (i+100000) < len(filedata) else len(filedata))]), 
            format='nt'
        )

        LOGGER.info(f'uploading {100000 if i + 100000 < len(filedata) else len(filedata) % 100000} triples')

        query = """
        INSERT DATA {
            GRAPH <http://localhost/%s> {
                %s
            } 
        }
        """ % (filename.with_suffix('').name ,g.serialize(format='nt'))

        sparql.setRequestMethod(POSTDIRECTLY)
        sparql.setQuery(query)
        sparql.query()

class GitBashOperator(BashOperator):
    """Clones/pulls a repo, extracts all/a subdir of the files, and copies them to a target dir.

    Args:
        repo_name (str): the name under which to store the repository data
        repo_url (str): the URL for the repo to be cloned
        target_dir (str): the directory to which data from the repo needs to be cloned
        sub_dir (str): the directory that contains the data to be copied, if not the root dir
    """

    template_fields = ('repo_name', 'repo_url', 'sub_dir', 'target_dir')

    @apply_defaults
    def __init__(
            self,
            repo_name,
            repo_url,
            target_dir,
            sub_dir = '.',
            *args, **kwargs):

        self.repo_name = repo_name
        self.repo_path = Path.home() / f'gitrepos/{self.repo_name}/'
        self.repo_url = repo_url
        self.target_dir = target_dir
        self.sub_dir = sub_dir
        
        super().__init__(bash_command='', *args, **kwargs)

    def execute(self, context):
        """First checks that all the correct dirs are in place. Checks if cloning is necessary
        or only (re-)pulling the existing repo. Then forms a bash command, handled by
        BashOperator which updates the repo, clears out the target dir, and copied in the
        data from the repo
        """
        LOGGER = logging.getLogger("airflow.task")
        LOGGER.info(f'preparing to pull {self.repo_url}')

        command = ''

        # Check if repo already exists and update command accordingly
        if not (self.repo_path / '.git').exists():
            LOGGER.info(f'repo does not exist yet - cloning it')
            self.repo_path.mkdir(parents=True, exist_ok=True)
            command = command + f'git clone {self.repo_url} {str(self.repo_path)} && '

        # Check if target dir exists
        if not self.target_dir.exists():
            LOGGER.info(f'target dir {str(self.target_dir)} does not exist yet - creating it')
            self.target_dir.mkdir(parents=True, exist_ok=True)

        self.bash_command = command + f'cd {str(self.repo_path)} && ' \
            'git checkout -- . && ' \
            'git pull && ' \
            f'cd {self.sub_dir} && ' \
            f'rm -rf {str(self.target_dir)}/* && ' \
            f'cp -Rf * {str(self.target_dir)}'
        
        # Have BashOperator actually execute the command
        return super().execute(context)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 0,
}

with DAG(
    'generate_triples',
    default_args=default_args,
    description='Generate a triples output file',
    schedule_interval=None,
    start_date=days_ago(0),
    catchup=False,
    max_active_runs=1
) as dag:

    fetch_r2rml_op = GitBashOperator(
        repo_name='r2rml_files_git',
        repo_url='https://gitlab.com/UM-CDS/protrait/mapping-unifications.git',
        target_dir=Path(os.environ['R2RML_DATA_DIR']) / 'settings/r2rml/',
        sub_dir='GenericList2',
        task_id='git',
    )

    # ./ontop materialize -m ../data/settings/mapping.ttl  -p ../data/settings/r2rml.properties.example -f ntriples -o ../data/output/triples.ttl
    generate_triples_op = BashOperator(
        task_id="generate_triples",
        bash_command= "if ls ${R2RML_DATA_DIR}/output/*.nt >/dev/null 2>&1; then rm ${R2RML_DATA_DIR}/output/*.nt; fi \n" +
        "for file in `basename ${R2RML_DATA_DIR}/settings/r2rml/*.ttl`; do \n" +
        "${R2RML_CLI_DIR}/ontop materialize " +
        "-m ${R2RML_DATA_DIR}/settings/r2rml/$file " +
        "-f ntriples " +
        "-p ${R2RML_DATA_DIR}/settings/r2rml.properties " +
        "-o ${R2RML_DATA_DIR}/output/$file \n" + 
        "done"
    )

    upload_triples_op = PythonOperator(
        task_id='upload_triples',
        python_callable=upload_triples_dir,
        op_kwargs={
            'input_path': Path(os.environ['R2RML_DATA_DIR']) / 'output', 
            'sparql_endpoint': os.environ['SPARQL_ENDPOINT']
            }
    )

    ontologies = {
        'roo': 'https://data.bioontology.org/ontologies/ROO/submissions/8/download?apikey=8b5b7825-538d-40e0-9e9e-5ab9274a9aeb',
        'ncit': 'https://data.bioontology.org/ontologies/NCIT/submissions/111/download?apikey=8b5b7825-538d-40e0-9e9e-5ab9274a9aeb',
    }

    for key, url in ontologies.items():
        op = PythonOperator(
            task_id=f'upload_ontology_{key}',
            python_callable=upload_terminology,
            op_kwargs={
                'url': url,
                'sparql_endpoint': os.environ['SPARQL_ENDPOINT']
            }
        )

        upload_triples_op >> op

    fetch_r2rml_op >> generate_triples_op >> upload_triples_op