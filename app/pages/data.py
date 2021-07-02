# -*- coding: utf-8 -*-

"""
FAIRifier's input data page
"""

import os
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
    html.H2('Upload new tables'),
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
    html.H2('Visualise tables'),
    html.P(),
    dcc.Dropdown(
        id='tables-dropdown',
        value=None,
        placeholder='Select a table'
    ),
    html.P(),
    html.Div(id='display-data'),
    html.P(),
    html.H2('Delete tables'),
    html.P(),
    dcc.Checklist(
        id='data-delete-input',
        labelStyle={'display': 'block'}
    ),
    html.P(),
    html.A(
        dcc.ConfirmDialogProvider(
            id='data-delete-button',
            children=html.Button('Delete'),
            message='Are you sure you want to delete?'
        ),
        href='/data'
    ),
    html.Div(
        id='hidden-div',
        style={'display':'none'}
    )
])


# ------------------------------------------------------------------------------
# Callbacks
# ------------------------------------------------------------------------------
@app.callback([Output('output-data-upload', 'children'),
               Output('tables-dropdown', 'options'),
               Output('data-delete-input', 'options')],
              [Input('data-upload', 'contents')],
              [State('data-upload', 'filename')])
def upload_tables(contents, filenames):

    # Upload new tables
    if contents:
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

    # List of saved tables for visualisation and deletion
    options = [{'label': o, 'value': o} for o in os.listdir('data')] \
        if os.path.exists('data') else []

    return children, options, options


@app.callback(Output('display-data', 'children'),
              Input('tables-dropdown', 'value'))
def display_table(filename):
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


@app.callback(Output('hidden-div', 'children'),
              [Input('data-delete-button', 'submit_n_clicks')],
              [State('data-delete-input', 'value')])
def delete_tables(delete, filenames):
    if (delete is not None) & (filenames is not None):
        for filename in filenames:
            os.remove(os.path.join('data', filename))
    return ''