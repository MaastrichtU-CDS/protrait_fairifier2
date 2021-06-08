from datetime import timedelta, datetime
import os
from pathlib import Path
import shutil
import zipfile
from glob import glob

from airflow import DAG
from airflow.models import taskinstance
from airflow.operators.bash_operator import BashOperator
from airflow.sensors.base_sensor_operator import BaseSensorOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.utils.dates import days_ago

class ZipSensor(BaseSensorOperator):
    """Waits for a zip to land in a filesystem.


    Args:
        BaseSensorOperator (Path): Where to wait for zip
    """
    def __init__(self, *, filepath, **kwargs):
        super().__init__(**kwargs)
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

def grab_input(input_dir, output_dir, **kwargs):
    """Look for a new zip file containing data and move it to the 'in_progress' dir

    Args:
        input_dir (Path): Where to look for zips
        output_dir (Path)): Where to put the zips
    """
    # TODO: Catch IndexError
    file = list(input_dir.glob('*.zip'))[0]

    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / file.name

    shutil.move(str(file.resolve()), str(output.resolve()))
    kwargs['ti'].xcom_push(key='archive_name', value=output.name)


def extract_files(input_dir, work_dir, **kwargs):
    """Extract files from the zip to a work directory
    Also creates a 'source_csv_files' xcom with locations of
    the extracted CSV files

    Args:
        input_dir (Path): Where to find the zip to extract
        work_dir (Path): What working dir to put the csv files in
    """
    work_dir.mkdir(parents=True, exist_ok=True)
    shutil.rmtree(str(work_dir.resolve()))
    work_dir.mkdir(parents=True, exist_ok=False)


    file = input_dir / kwargs['ti'].xcom_pull(task_ids='move_to_in_progress', key='archive_name')
    archive = zipfile.ZipFile(file)
    archive.extractall(path=work_dir)
    filenames = archive.namelist()
    filenames = [str(work_dir / name) for name in filenames if not '/' in name]

    kwargs['ti'].xcom_push(key='source_csv_files', value=';'.join(filenames))

def cleanup(input_dir, work_dir, output_dir, **kwargs):
    """Cleans up the working directory and moves the zips to a 'done' dir

    Args:
        input_dir (Path): Where are the zips?
        work_dir (Path): Where were the csv's stored?
        output_dir (Path): Where to store the zips?
    """
    shutil.rmtree(str(work_dir.resolve()))

    archive = input_dir / kwargs['ti'].xcom_pull(task_ids='move_to_in_progress', key='archive_name')
    dest = output_dir / (archive.name + '.' + kwargs['ts_nodash'])
    shutil.move(str(archive), str(dest))


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 0,
}

r2rml_dir = Path(os.environ['R2RML_DATA_DIR'])

with DAG(
    'create_triples',
    default_args=default_args,
    description='Generates triples files from R2RML scripts and CSV files',
    schedule_interval=timedelta(minutes=1),
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

    move_from_source_op = PythonOperator(
        python_callable=grab_input,
        task_id="move_to_in_progress",
        op_kwargs={
            'input_dir': r2rml_dir / 'input',
            'output_dir': r2rml_dir / 'input' / 'in_progress'
        },
        provide_context=True
    )

    extract_files_op = PythonOperator(
        python_callable=extract_files,
        task_id="extract_files",
        op_kwargs={
            'input_dir': r2rml_dir / 'input' / 'in_progress',
            'work_dir': Path('/tmp/csv')
        },
        provide_context=True
    )

    generate_triples_op = BashOperator(
        bash_command="java -jar ${R2RML_CLI_DIR}/r2rml.jar " +
            '--CSVFiles="{{task_instance.xcom_pull(task_ids="extract_files", key="source_csv_files")}}" ' +
            "--outputFile=" + str(r2rml_dir / 'output' / 'output.ttl') + " " +
            "--mappingFile=${R2RML_DATA_DIR}/settings/mapping.ttl " +
            "--format=TURTLE " +
            '--baseIRI="http://localhost/"',
            task_id='generate_triples',
        provide_context=True
    )

    move_to_done_op = PythonOperator(
        python_callable=cleanup,
        task_id="cleanup",
        op_kwargs={
            'input_dir': r2rml_dir / 'input' / 'in_progress',
            'work_dir': Path('/tmp/csv'),
            'output_dir': r2rml_dir / 'input' / 'done'
        },
        provide_context=True
    )

    sense_input >> move_from_source_op >> extract_files_op >> generate_triples_op >> move_to_done_op 