import os
from datetime import datetime
from glob import glob
from pathlib import Path
from uuid import uuid4
from typing import Optional, Dict
import shutil

from airflow.sensors.base_sensor_operator import BaseSensorOperator
from airflow.operators.bash_operator import BashOperator


def setup_tmp_dir(**kwargs):
    ti = kwargs['task_instance']
    dir_name = Path('/tmp/') / str(uuid4())
    dir_name.mkdir(parents=True, exist_ok=False)

    ti.xcom_push(key='working_dir', value=str(dir_name))

    return str(dir_name)

def remove_tmp_dir(dir, **kwargs):
    shutil.rmtree(dir)


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

class GitCloneOperator(BashOperator):
    def __init__(self,
                *,
                 repo_name,
                 repo_url,
                 target_dir,
                 repo_path,
                 sub_dir = '.',
                 env: Optional[Dict[str, str]] = None, 
                 skip_exit_code: int = 99, 
                 **kwargs) -> None:

        bash_command = 'mkdir -p $repo_path ; ' \
            'mkdir -p $target_dir ; ' \
            'git clone $repo_url $repo_path && ' \
            'cd $repo_path && ' \
            'cd $sub_dir && ' \
            'rm -rf ${target_dir}/* && ' \
            'cp -Rf * $target_dir'
        
        if not env:
            env = {}

        env.setdefault('repo_name',repo_name)
        env.setdefault('repo_url',repo_url)
        env.setdefault('target_dir',target_dir)
        env.setdefault('repo_path',repo_path)
        env.setdefault('sub_dir',sub_dir)

        super().__init__(bash_command=bash_command, env=env, skip_exit_code=skip_exit_code, **kwargs)