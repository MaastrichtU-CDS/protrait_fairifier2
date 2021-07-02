# -*- coding: utf-8 -*-

"""
FAIRifier's annotations page
"""

import dash_table

import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd

from dash.dependencies import Input
from dash.dependencies import Output

from app import app


inputs = None
# ------------------------------------------------------------------------------
# Annotations page layout
# ------------------------------------------------------------------------------
layout = html.Div([
    html.H1('Terminology mapping'),
    html.Hr(),
    html.P(),
    dbc.DropdownMenu(
        id='input-column',
        label='Select a column:',
        children=[
            dbc.DropdownMenuItem('Test1'),
            dbc.DropdownMenuItem('Test2')
        ],
    ),
    html.Div(id='output-annotation'),
])


# ------------------------------------------------------------------------------
# Callbacks
# ------------------------------------------------------------------------------
@app.callback(Output('output-annotation', 'children'),
              Input('input-column', 'value'))
def update_annotations(column):
    # TODO: implement multiple files option
    if inputs is not None:
        df2 = inputs[list(inputs.keys())[0]]
        local_terms = df2['vital_status'].unique()
        df = pd.DataFrame({
            'Local term': local_terms,
            'Target class:': ['alive']*len(local_terms),
            'Super class': ['vital status']*len(local_terms),
        })

        return html.Div([
            html.P(),
            dash_table.DataTable(
                id='table-dropdown',
                data=df.to_dict('records'),
                columns=[
                    {'id': 'Local term', 'name': 'Local term'},
                    {'id': 'Target class', 'name': 'Target class',
                     'presentation': 'dropdown'},
                    {'id': 'Super class', 'name': 'Super class',
                     'presentation': 'dropdown'}
                ],
                editable=True,
                dropdown={
                    'Target class': {
                        'options': [
                            {'label': i, 'value': i} for i in ['alive', 'dead']
                        ]
                    },
                    'Super class': {
                        'options': [
                            {'label': i, 'value': i}
                            for i in ['vital status', 'B']
                        ]
                    }
                }
            ),
            html.Div(id='table-dropdown-container')
        ])
    else:
        return html.P('Please upload a file!')