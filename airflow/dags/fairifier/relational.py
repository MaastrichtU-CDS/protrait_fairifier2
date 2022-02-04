import zipfile
import shutil

import pandas as pd
from sqlalchemy.engine import create_engine


def extract_zip_and_upload_rdb(input_dir, success_dir, conn_str, append=True, **kwargs):
    """Take in a zip of CSV files and upload them to the database

    Args:
        input_dir (Path): Path to the directory containing incoming zips
        success_dir (Path): Directory where successfully parsed zips should go
        error_dir (Path): Directory where failed parsed zips should go

    """
    file = list(input_dir.glob('*.zip'))[0]

    success_dir.mkdir(parents=True, exist_ok=True)

    archive = zipfile.ZipFile(file)
    csv_names = archive.namelist()

    eng = create_engine(conn_str)

    # TODO better checking of filetypes
    for name in csv_names:
        if '/' not in name and name.endswith('.csv'):
            df = pd.read_csv(archive.open(name))

            df.to_sql(name.split('.')[0], eng, if_exists='append' if append else 'replace')

    shutil.move(str(file.resolve()), str((success_dir / (file.name + '.' + kwargs['ts_nodash'])).resolve()))
