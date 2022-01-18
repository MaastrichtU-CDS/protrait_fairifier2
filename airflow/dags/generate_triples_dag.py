from datetime import timedelta, datetime
from pathlib import Path
import os
import logging
import requests
from uuid import uuid4

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

    input_path = Path(input_path)

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
        sparql = SPARQLWrapper(sparql_endpoint + '/statements')

        LOGGER.info(f'starting upload to {sparql_endpoint}')
        g = rdf.Graph()
        g.parse(data=ret.text, format='xml')
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

def initialize(**kwargs):
    ti = kwargs['task_instance']
    dir_name = Path('/tmp/') / str(uuid4())
    dir_name.mkdir(parents=True, exist_ok=False)

    ti.xcom_push(key='working_dir', value=str(dir_name))


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

    setup_op = PythonOperator(
        task_id='initialize',
        python_callable=initialize,
        provide_context=True
    )

    fetch_r2rml_op = BashOperator(
        task_id='get_r2rml_files',
        bash_command = 'mkdir -p $repo_path ; ' \
            'mkdir -p $target_dir ; ' \
            'git clone $repo_url $repo_path && ' \
            'cd $repo_path && ' \
            'cd $sub_dir && ' \
            'rm -rf ${target_dir}/* && ' \
            'cp -Rf * $target_dir',
        env={
            'repo_name': 'r2rml_files_git',
            'repo_url': 'https://github.com/jaspersnel/r2rml_tests.git',
            'target_dir': '{{ ti.xcom_pull(key="working_dir", task_ids="initialize") }}/ttl',
            'repo_path': '{{ ti.xcom_pull(key="working_dir", task_ids="initialize") }}/gitrepos/ttl',
            'sub_dir': '.',
        }
    )

    # ./ontop materialize -m ../data/settings/mapping.ttl  -p ../data/settings/r2rml.properties.example -f ntriples -o ../data/output/triples.ttl
    # TODO: move r2rml.properties to  CLI_DIR
    generate_triples_op = BashOperator(
        task_id="generate_RDF_triples",
        bash_command= "mkdir -p ${workdir}/output \n" +
            "if ls ${workdir}/output/*.nt >/dev/null 2>&1; " + 
            "then rm ${workdir}/output/*.nt; "+
            "fi \n" +
            "for file in `basename ${workdir}/ttl/*.ttl`; "+
            "do \n" +
            "${R2RML_CLI_DIR}/ontop materialize " +
            "-m ${workdir}/ttl/$file " +
            "-f ntriples " +
            "-p ${R2RML_CLI_DIR}/r2rml.properties " +
            "-o ${workdir}/output/$file \n" + 
            "done",
        env={
            'workdir': "{{ ti.xcom_pull(key='working_dir', task_ids='initialize') }}",
            'R2RML_CLI_DIR': os.environ.get('R2RML_CLI_DIR')
        }
    )

    upload_triples_op = PythonOperator(
        task_id='upload_to_graphDB',
        python_callable=upload_triples_dir,
        op_kwargs={
            'input_path': '{{ ti.xcom_pull(key="working_dir", task_ids="initialize") }}/output', 
            'sparql_endpoint': os.environ['SPARQL_ENDPOINT']
            }
    )

    ontologies = {
        'roo': 'https://data.bioontology.org/ontologies/ROO/submissions/8/download?apikey=8b5b7825-538d-40e0-9e9e-5ab9274a9aeb',
        #'ncit': 'https://data.bioontology.org/ontologies/NCIT/submissions/111/download?apikey=8b5b7825-538d-40e0-9e9e-5ab9274a9aeb',
    }

    finalize_op = BashOperator(
        task_id='finalize',
        bash_command='rm -rf {{ ti.xcom_pull(key="working_dir", task_ids="initialize") }}',
        trigger_rule='all_done',
    )


    for key, url in ontologies.items():
        op = PythonOperator(
            task_id=f'upload_ontology_{key}',
            python_callable=upload_terminology,
            op_kwargs={
                'url': url,
                'sparql_endpoint': os.environ['SPARQL_ENDPOINT']
            }
        )

        upload_triples_op >> op >> finalize_op

    setup_op >> fetch_r2rml_op >> generate_triples_op >> upload_triples_op