# -*- coding: utf-8 -*-

"""
Module with database functionalities
"""

import pandas as pd
from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class ManageDB:
    """ Class for interaction with database
    """

    def __init__(self, dbname, host, port, user, password):
        """ Initialisation method of ManageDB class

        Parameters
        ----------
        dbname : str
            Database name
        host : str
            Host address
        port : int
            Connection port number
        user : str
            Database username
        password : str
            User's password
        """
        self.dbname = dbname
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def connect(self):
        """ Connect to database
        """
        try:
            self.conn = connect(
                dbname=self.dbname,
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password
            )
            self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        except Exception as e:
            raise Exception(f'Unable to connect to the database: {e}')

    def create_table(self, table, columns):
        """ Create a new table

        Parameters
        ----------
        table : str
            Table name
        columns : dict
            Dictionary with column names as keys and their types as values
        """
        try:
            # Open cursor to perform database operation
            cursor = self.conn.cursor()

            # Flatten dictionary with columns to a string
            columns = ','.join(map(' '.join, columns.items()))

            # Create table
            create_table = f'CREATE TABLE %s (%s);' % (table, columns)
            cursor.execute(create_table)
        except Exception as e:
            raise Exception(f'Unable to create table: {e}')

    def prepare_data(self, file_path, columns, rename=None):
        """ Prepare data from CSV input

        Parameters
        ----------
        file_path : str
            Path to csv file
        columns : list
            List with relevant columns
        rename : dict
            Dictionary with mapping for column names

        Returns
        -------
        df : pd.DataFrame
            Dataframe with input data
        """

        # Read csv file
        df = pd.read_csv(file_path)

        # Rename columns when necessary
        if rename:
            df.rename(columns=rename, inplace=True)

        # Make sure that columns are in the correct order and that only
        # relevant ones are selected
        df = df[columns]

        return df

    def insert_data(self, table, columns, df):
        """ Insert new data into table

        Parameters
        ----------
        table : str
            Table name
        columns : list
            List with column names
        df : pd.DataFrame
            Dataframe with data to be inserted, we assume that the columns
            are in the correct order
        """
        try:
            # Open cursor to perform database operation
            cursor = self.conn.cursor()

            # Insertion statement
            # TODO: retrieve column names automatically?
            cols = ', '.join(columns)
            values = ', '.join(['%s']*df.shape[1])
            insert = f'INSERT INTO %s (%s) VALUES (%s)' % (table, cols, values)

            # Insert new data
            for index, row in df.iterrows():
                cursor.execute(insert, tuple(row.values))

            # Commit data insertion
            self.conn.commit()
        except Exception as e:
            raise Exception(f'Unable to insert new data: {e}')

    def show_table(self, table, n=10):
        """ Display top n rows of a table

        Parameters
        ----------
        table : str
            Table name
        n : int
            Number of rows to display
        """
        try:
            # Open cursor to perform database operation
            cursor = self.conn.cursor()

            # Query table
            query = f'SELECT * FROM %s;' % table
            cursor.execute(query)
            results = cursor.fetchall()

            # Display results
            for row in results[:n]:
                print(row)
        except Exception as e:
            raise Exception(f'Unable to display table: {e}')

    def close(self):
        """ Close database connection
        """
        self.conn.close()
