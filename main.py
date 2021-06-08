# -*- coding: utf-8 -*-

"""
FAIRification data pipeline
"""

import os
from src.manage_db import ManageDB
from src.manage_r2rml import ManageR2RML


if __name__ == '__main__':

    # Relational database params
    dbname = 'postgresdb'
    host = 'localhost'
    port = 5432
    user = 'postgres'
    password = '12345'
    table = 'PBDWHackathon2018'
    columns = {
        'ID': 'text PRIMARY KEY',
        'PatientID': 'text',
        'Age': 'text',
        'Gender': 'text',
        'Clinical_T_Stage': 'text',
        'Clinical_N_Stage': 'text',
        'SurvivalTime': 'text',
        'DeadStatus': 'text'
    }
    rename = {
        'Sex': 'Gender',
        'Clinical.T.Stage': 'Clinical_T_Stage',
        'Clinical.N.Stage': 'Clinical_N_Stage',
        'Survival.Time.Days': 'SurvivalTime',
        'deadstatus.event': 'DeadStatus'
    }
    file_path = 'data/Clinical1.csv'

    # Insert data to postgres database
    postgres = ManageDB(
        dbname=dbname, host=host, port=port, user=user, password=password
    )
    postgres.connect()
    postgres.create_table(table=table, columns=columns)
    df = postgres.prepare_data(file_path=file_path, columns=columns.keys(),
                               rename=rename)
    postgres.insert_data(table=table, columns=df.columns, df=df)
    postgres.show_table(table=table)
    postgres.close()
    print(f'Inserted data to postgres database')

    # Load RDF mapping file
    graphdb_base_url = 'http://localhost:7200/repositories/'
    r2rml_endpoint = os.path.join('r2rml', 'statements')
    mapping_file = 'data/mapping_test.ttl'
    r2rml = ManageR2RML(
        graphdb_base_url=graphdb_base_url, r2rml_endpoint=r2rml_endpoint,
        mapping_file=mapping_file
    )
    r2rml.drop_rdf_mappings()
    r2rml.load_rdf_mapping()
    r2rml.insert_rdf_mapping()
    print(f'Loaded RDF mapping')

