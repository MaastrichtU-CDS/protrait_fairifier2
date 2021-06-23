from datetime import timedelta, datetime
from glob import glob
from pathlib import Path
import os

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

import rdflib as rdf
from SPARQLWrapper import SPARQLWrapper, POSTDIRECTLY


def upload_triples(input_path, sparql_endpoint, **kwargs):
    sparql = SPARQLWrapper(sparql_endpoint + '/statements')

    for file in input_path.glob('*.nt'):
        g = rdf.Graph()
        g.load(str(file.resolve()), format='nt')

        deleteQuery = """
            CLEAR GRAPH <http://localhost/%s>
        """ % (file.with_suffix('').name)

        sparql.setQuery(deleteQuery)
        sparql.query()

        query = """
        INSERT DATA {
            GRAPH <http://localhost/%s> {
                %s
            } 
        }
        """ % (file.with_suffix('').name ,g.serialize(format='nt').decode())

        sparql.setRequestMethod(POSTDIRECTLY)
        sparql.setQuery(query)
        sparql.query()

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

    # ./ontop materialize -m ../data/settings/mapping.ttl  -p ../data/settings/r2rml.properties.example -f ntriples -o ../data/output/triples.ttl
    generate_triples_op = BashOperator(
        task_id="generate_triples",
        bash_command="${R2RML_CLI_DIR}/ontop materialize " +
        "-m ${R2RML_DATA_DIR}/settings/mapping.ttl " +
        "--db-url jdbc:${R2RML_DB_URL}" +
        "-f ntriples " +
        "-o ${R2RML_DATA_DIR}/output/output.ttl "
    )

    upload_triples_op = PythonOperator(
        task_id='upload_triples',
        python_callable=upload_triples,
        op_kwargs={
            'input_path': Path(os.environ['R2RML_DATA_DIR']) / 'output', 
            'sparql_endpoint': os.environ['SPARQL_ENDPOINT']
            }
    )

    generate_triples_op >> upload_triples_op