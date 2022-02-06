from pathlib import Path
import logging
from typing import Optional, Dict

import rdflib as rdf
from SPARQLWrapper import SPARQLWrapper, POSTDIRECTLY

from airflow.operators.bash_operator import BashOperator


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

def upload_terminology(url, sparql_endpoint, format='xml', **kwargs):
    """Uploads a given ontology file to the SPARQL endpoint
    
    """
    LOGGER = logging.getLogger("airflow.task")
    LOGGER.info(f'downloading file {url}')

    sparql = SPARQLWrapper(sparql_endpoint + '/statements')

    LOGGER.info(f'starting upload to {sparql_endpoint}')
    g = rdf.Graph()
    g.parse(url, format=format)
    triples_lines = g.serialize(format='nt').split('\n')

    for i in range(0, len(triples_lines), 100000):
        LOGGER.info(f'uploading {100000 if i + 100000 < len(triples_lines) else len(triples_lines) % 100000} triples')

        query = """
        INSERT DATA {
            GRAPH <http://localhost/ontology> {
                %s
            } 
        }
        """ % ('\n'.join(triples_lines[i:(i + 100000 if (i+100000) < len(triples_lines) else len(triples_lines))]))

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

class OntOperator(BashOperator):    
    def __init__(self,
                 workdir,
                 r2rml_cli_dir,
                 rdb_connstr,
                 rdb_user,
                 rdb_pass,
                 env: Optional[Dict[str, str]] = {}, 
                 skip_exit_code: int = 99, 
                 **kwargs) -> None:

        rdb_connstr = rdb_connstr.replace(':', r'\:')

        bash_command = 'echo "jdbc.name=r2rml" > ${workdir}/r2rml.properties ; ' +\
            f'echo "jdbc.url={rdb_connstr}"' + ' >> ${workdir}/r2rml.properties ; ' +\
            f'echo "jdbc.user={rdb_user}"' + ' >> ${workdir}/r2rml.properties ; ' +\
            f'echo "jdbc.password={rdb_pass}"' + ' >> ${workdir}/r2rml.properties\n'

        bash_command= bash_command + "mkdir -p ${workdir}/output \n" +\
            "if ls ${workdir}/output/*.nt >/dev/null 2>&1; " +\
            "then rm ${workdir}/output/*.nt; " +\
            "fi \n" +\
            "for file in `basename ${workdir}/ttl/*.ttl`; " +\
            "do \n" +\
            "${R2RML_CLI_DIR}/ontop materialize " +\
            "-m ${workdir}/ttl/$file " +\
            "-f ntriples " +\
            "-p ${workdir}/r2rml.properties " +\
            "-o ${workdir}/output/$file \n" +\
            "done"
        
        env.setdefault('workdir', workdir)
        env.setdefault('R2RML_CLI_DIR', r2rml_cli_dir)

        super().__init__(bash_command=bash_command, env=env, skip_exit_code=skip_exit_code, **kwargs)