# -*- coding: utf-8 -*-

"""
FAIRification data pipeline
"""

from src.manage_db import ManageDB


if __name__ == '__main__':

    # Database params
    dbname = 'postgresdb'
    host = 'localhost'
    port = 5432
    user = 'postgres'
    password = '12345'

    # Connect to database
    postgres = ManageDB(
        dbname=dbname, host=host, port=port, user=user, password=password
    )
    postgres.connect()

    # Create new table
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
    postgres.create_table(table=table, columns=columns)

    # Prepare data
    file_path = 'data/20k_sample_data.csv'
    df = postgres.prepare_data(file_path=file_path, columns=columns.keys())

    # Insert data to table
    postgres.insert_data(table=table, columns=columns.keys(), df=df)
    print('All worked out')

    # Display table
    postgres.show_table(table=table)

    # Close database
    postgres.close()

