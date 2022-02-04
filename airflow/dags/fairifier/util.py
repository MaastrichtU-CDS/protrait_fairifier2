import os
from datetime import datetime
from glob import glob

from airflow.sensors.base_sensor_operator import BaseSensorOperator


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

