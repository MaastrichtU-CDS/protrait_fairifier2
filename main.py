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
    table = 'CORALDATA'
    columns = {
        'id': 'text PRIMARY KEY',
        't': 'text',
        'n': 'text',
        'm': 'text',
        'stage': 'text',
        'date_of_diagnosis': 'text',
        'date_of_fu': 'text',
        'vital_status': 'text'
    }
    file_path = 'data/20k_sample_data.csv'

    # Insert data to postgres database
    postgres = ManageDB(
        dbname=dbname, host=host, port=port, user=user, password=password
    )
    postgres.connect()
    postgres.create_table(table=table, columns=columns)
    df = postgres.prepare_data(file_path=file_path, columns=columns.keys())
    postgres.insert_data(table=table, columns=columns.keys(), df=df)
    postgres.show_table(table=table)
    postgres.close()
    print(f'Inserted data to postgres database')

    # Load RDF mapping file
    graphdb_base_url = 'http://localhost:7200/repositories/'
    r2rml_endpoint = os.path.join('r2rml', 'statements')
    mapping_file = 'data/mapping.ttl'
    r2rml = ManageR2RML(
        graphdb_base_url=graphdb_base_url, r2rml_endpoint=r2rml_endpoint,
        mapping_file=mapping_file
    )
    r2rml.drop_rdf_mappings()
    #r2rml.load_rdf_mapping()
    #r2rml.insert_rdf_mapping()
    #print(f'Loaded RDF mapping')

