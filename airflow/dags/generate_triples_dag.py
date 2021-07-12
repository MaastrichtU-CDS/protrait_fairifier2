from datetime import timedelta, datetime
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

    deleteQuery = """
            DELETE {?s ?p ?o} WHERE {?s ?p ?o}
        """

    sparql.setQuery(deleteQuery)
    sparql.query()

    for file in input_path.glob('*.nt'):
        with open(file, 'r') as f:
            filedata = f.readlines()

        for i in range(0, len(filedata), 100000):
            g = rdf.Graph()
            g.parse(
                data='\n'.join(filedata[i:(i + 100000 if (i+100000) < len(filedata) else len(filedata))]), 
                format='nt'
            )

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
        bash_command="for file in `basename ${R2RML_DATA_DIR}/settings/*.ttl`; do \n" +
        "${R2RML_CLI_DIR}/ontop materialize " +
        "-m ${R2RML_DATA_DIR}/settings/$file " +
        "-f ntriples " +
        "-p ${R2RML_DATA_DIR}/settings/r2rml.properties " +
        "-o ${R2RML_DATA_DIR}/output/$file \n" + 
        "done"
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