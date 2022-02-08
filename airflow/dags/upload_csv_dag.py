from datetime import timedelta
from pathlib import Path

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable

from fairifier.util import ZipSensor
from fairifier.relational import extract_zip_and_upload_rdb


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 0,
}

data_dir = Path(Variable.get('USER_DATA_DIR'))

with DAG(
    'upload_csv',
    default_args=default_args,
    description='Generates triples files from R2RML scripts and CSV files',
    # schedule_interval=timedelta(minutes=1),
    schedule_interval=None,
    start_date=days_ago(0),
    catchup=False,
    max_active_runs=1
) as dag:

    sense_input = ZipSensor(
        task_id="sense_input",
        filepath=data_dir / 'input',
        mode='poke',
        timeout=60,
        poke_interval=5,
        soft_fail=True
    )

    extract_and_upload_op = PythonOperator(
        python_callable=extract_zip_and_upload_rdb,
        task_id="extract_and_upload",
        op_kwargs={
            'input_dir': data_dir / 'input',
            'success_dir': data_dir / 'input' / 'done',
            'conn_str': Variable.get('RDB_CONNSTR'),
            'append': int(Variable.get('APPEND_CSV', 1))
        },
        provide_context=True
    )

    trigger_triples_op = TriggerDagRunOperator(
        task_id="trigger_triples",
        trigger_dag_id='generate_triples'
    )

    trigger_self_op = TriggerDagRunOperator(
        task_id="reschedule",
        reset_dag_run=True,
        trigger_dag_id='upload_csv',
    )

    sense_input >> extract_and_upload_op >> trigger_triples_op >> trigger_self_op