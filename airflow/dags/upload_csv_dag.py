from datetime import timedelta, datetime
import os
from pathlib import Path
import shutil
import zipfile
from glob import glob

from airflow import DAG
from airflow.sensors.base_sensor_operator import BaseSensorOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

import pandas as pd
from sqlalchemy.engine import create_engine

class ZipSensor(BaseSensorOperator):
    """Waits for a zip to land in a filesystem.


    Args:
        BaseSensorOperator (Path): Where to wait for zip
    """
    def __init__(self, *, filepath, **kwargs):
        super().__init__(**kwargs)

        # Look just for zips
        self.filepath = filepath / '*.zip'

    def poke(self, context):
        self.log.info('Poking for file %s', self.filepath)

        for path in glob(str(self.filepath)):
            if os.path.isfile(path):
                mod_time = os.path.getmtime(path)
                mod_time = datetime.fromtimestamp(mod_time).strftime('%Y%m%d%H%M%S')
                self.log.info('Found File %s last modified: %s', str(path), str(mod_time))
                return True

        return False

def extract_and_upload(input_dir, success_dir, error_dir, append, **kwargs):
    """Take in a zip of CSV files and upload them to the database
        TODO: implement error dir

    Args:
        input_dir (Path): Path to the directory containing incoming zips
        success_dir (Path): Directory where successfully parsed zips should go
        error_dir (Path): Directory where failed parsed zips should go

    """
    file = list(input_dir.glob('*.zip'))[0]

    success_dir.mkdir(parents=True, exist_ok=True)
    error_dir.mkdir(parents=True, exist_ok=True)

    archive = zipfile.ZipFile(file)
    csv_names = archive.namelist()

    eng = create_engine(f'postgresql://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASSWORD"]}@postgres:5432/data')

    # TODO better checking of filetypes
    for name in csv_names:
        if '/' not in name and name.endswith('.csv'):
            df = pd.read_csv(archive.open(name))

            df.to_sql(name.split('.')[0], eng, if_exists='append' if append else 'replace')

    shutil.move(str(file.resolve()), str((success_dir / (file.name + '.' + kwargs['ts_nodash'])).resolve()))


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 0,
}

r2rml_dir = Path(os.environ['R2RML_DATA_DIR'])

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
        filepath=r2rml_dir / 'input',
        mode='poke',
        timeout=60,
        poke_interval=5,
        soft_fail=True
    )

    extract_and_upload_op = PythonOperator(
        python_callable=extract_and_upload,
        task_id="extract_and_upload",
        op_kwargs={
            'input_dir': r2rml_dir / 'input',
            'success_dir': r2rml_dir / 'input' / 'done',
            'error_dir': r2rml_dir / 'input' / 'error',
            'append': os.environ.get('APPEND_CSV', 0)
        },
        provide_context=True
    )

    sense_input >> extract_and_upload_op 