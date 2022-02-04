from datetime import timedelta, datetime
from pathlib import Path
import os
from uuid import uuid4

from airflow import DAG
from airflow.utils.decorators import apply_defaults
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from fairifier.rdf import upload_triples_dir, upload_terminology
from fairifier.util import setup_tmp_dir


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
            'repo_url': os.environ['R2RML_REPO'],
            'target_dir': '{{ ti.xcom_pull(key="working_dir", task_ids="initialize") }}/ttl',
            'repo_path': '{{ ti.xcom_pull(key="working_dir", task_ids="initialize") }}/gitrepos/ttl',
            'sub_dir': os.environ['R2RML_REPO_SUBDIR'],
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