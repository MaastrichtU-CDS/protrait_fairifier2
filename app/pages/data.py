# -*- coding: utf-8 -*-

"""
FAIRifier's input data page
"""

import os
import datetime
import dash_table

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State

from app import app
from data_processing.input_data import parse_content


# ------------------------------------------------------------------------------
# Input data page layout
# ------------------------------------------------------------------------------
layout = html.Div([
    html.H1('Data'),
    html.Hr(),
    html.P(),
    html.H2('Upload new data:'),
    html.P(),
    dcc.Upload(
        id='data-upload',
        children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=True
    ),
    html.Div(id='output-data-upload'),
    html.P(),
    html.H2('Current data:'),
    html.P(),
    dcc.Dropdown(
        id='tables-dropdown',
        value=None,
        placeholder='Select a table'
    ),
    html.P(),
    html.Div(id='display-data')
])


# ------------------------------------------------------------------------------
# Callbacks
# ------------------------------------------------------------------------------
@app.callback([Output('output-data-upload', 'children'),
               Output('tables-dropdown', 'options')],
              Input('data-upload', 'contents'),
              State('data-upload', 'filename'))
def data_upload(contents, filenames):
    if contents is not None:
        children = []
        for content, filename in zip(contents, filenames):

            # Parse data
            df = parse_content(content, filename)

            # Add .csv extension in case of excel file
            if '.xls' in filename:
                filename = filename + '.csv'

            # Save data
            filepath = os.path.join('data', filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            df.to_csv(filepath, index=False, encoding='utf-8')

            # Success message
            children.append(html.P(f'File %s uploaded' % filename))
    else:
        children = html.P()

    # Dropdown with saved tables
    options = [{'label': o, 'value': o} for o in os.listdir('data')] \
        if os.path.exists('data') else []

    return children, options


@app.callback(Output('display-data', 'children'),
              Input('tables-dropdown', 'value'))
def display_data(filename):
    if filename is not None:
        # Read data
        filepath = os.path.join('data', filename)
        df = pd.read_csv(filepath)

        # Display first lines of table
        return html.Div([
            dash_table.DataTable(
                data=df[:5].to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df.columns]
            )
        ])
    else:
        return html.P()
