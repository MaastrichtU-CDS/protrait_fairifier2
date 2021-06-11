from datetime import timedelta, datetime
from glob import glob

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


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
        "-p ${R2RML_DATA_DIR}/settings/r2rml.properties " +
        "-f ntriples " +
        "-o ${R2RML_DATA_DIR}/output/output.ttl "
    )