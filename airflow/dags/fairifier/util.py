import os
from datetime import datetime
from glob import glob
from pathlib import Path
from uuid import uuid4

from airflow.sensors.base_sensor_operator import BaseSensorOperator


def setup_tmp_dir(**kwargs):
    ti = kwargs['task_instance']
    dir_name = Path('/tmp/') / str(uuid4())
    dir_name.mkdir(parents=True, exist_ok=False)

    ti.xcom_push(key='working_dir', value=str(dir_name))

    return str(dir_name)

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

