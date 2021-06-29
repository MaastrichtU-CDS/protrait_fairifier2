# -*- coding: utf-8 -*-

"""
Module with input data functionalities
"""

import io
import base64
import dash_table

import pandas as pd
import dash_html_components as html


def parse_content(content, filename):

    # Decode content
    content_type, content_string = content.split(',')
    decoded = base64.b64decode(content_string)

    # Read input data
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except:
        # TODO: not catching exception properly
        df = None

    return df


def display_data(filename, df):
    if df is None:
        return html.Div([
            html.P(),
            html.P('Not able to parse the file: %s' % filename),
            html.Hr()
        ])
    else:
        return html.Div([
            html.P(),
            html.H5('Uploaded file: %s' % filename),
            dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df.columns]
            ),
            html.Hr()
        ])
