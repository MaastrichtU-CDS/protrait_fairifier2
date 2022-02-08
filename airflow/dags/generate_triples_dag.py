from datetime import timedelta
import os

from airflow import DAG
from airflow.utils.decorators import apply_defaults
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable

from fairifier.rdf import upload_triples_dir, upload_terminology, OntOperator
from fairifier.util import setup_tmp_dir, remove_tmp_dir, GitCloneOperator


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
        python_callable=setup_tmp_dir,
        provide_context=True
    )

    fetch_r2rml_op = GitCloneOperator(
        task_id='get_r2rml_files',
        repo_name = 'r2rml_files_git',
        repo_url = Variable.get('R2RML_REPO'),
        target_dir = '{{ ti.xcom_pull(key="working_dir", task_ids="initialize") }}/ttl',
        repo_path = '{{ ti.xcom_pull(key="working_dir", task_ids="initialize") }}/gitrepos/ttl',
        sub_dir = Variable.get('R2RML_REPO_SUBDIR'),
    )

    generate_triples_op = OntOperator(
        task_id="generate_RDF_triples",
        workdir = "{{ ti.xcom_pull(key='working_dir', task_ids='initialize') }}",
        r2rml_cli_dir = Variable.get('R2RML_CLI_DIR'),
        rdb_connstr = Variable.get('RDB_CONNSTR'),
        rdb_user=Variable.get('RDB_USER'),
        rdb_pass=Variable.get('RDB_PASSWORD')
    )

    upload_triples_op = PythonOperator(
        task_id='upload_to_graphDB',
        python_callable=upload_triples_dir,
        op_kwargs={
            'input_path': '{{ ti.xcom_pull(key="working_dir", task_ids="initialize") }}/output', 
            'sparql_endpoint': Variable.get('SPARQL_ENDPOINT')
            }
    )

    ontologies = {
        'roo': 'https://data.bioontology.org/ontologies/ROO/submissions/8/download?apikey=8b5b7825-538d-40e0-9e9e-5ab9274a9aeb',
        #'ncit': 'https://data.bioontology.org/ontologies/NCIT/submissions/111/download?apikey=8b5b7825-538d-40e0-9e9e-5ab9274a9aeb',
    }

    finalize_op = PythonOperator(
        task_id='finalize',
        python_callable=remove_tmp_dir,
        op_kwargs={
            'dir': '{{ ti.xcom_pull(key="working_dir", task_ids="initialize") }}',
        },
        trigger_rule='all_done',
    )


    for key, url in ontologies.items():
        op = PythonOperator(
            task_id=f'upload_ontology_{key}',
            python_callable=upload_terminology,
            op_kwargs={
                'url': url,
                'sparql_endpoint': Variable.get('SPARQL_ENDPOINT')
            }
        )

        upload_triples_op >> op >> finalize_op

    setup_op >> fetch_r2rml_op >> generate_triples_op >> upload_triples_op