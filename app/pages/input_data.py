# -*- coding: utf-8 -*-

"""
FAIRifier's input data page
"""

import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State

from app import app
from data_processing.input_data import parse_content
from data_processing.input_data import display_data


# TODO: these don't need to be global vars
inputs = None
children = None

# ------------------------------------------------------------------------------
# Input data page layout
# ------------------------------------------------------------------------------
layout = html.Div([
    html.H1('Upload your data'),
    html.Hr(),
    html.P(),
    dcc.Upload(
        id='upload-data',
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
])


# ------------------------------------------------------------------------------
# Callbacks
# ------------------------------------------------------------------------------
@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'))
def update_data_upload(contents, filenames):
    global inputs
    global children
    if contents is not None:
        inputs = {
            filename: parse_content(content, filename)
            for content, filename in zip(contents, filenames)
        }
    if inputs is not None:
        children = [
            display_data(filename, df) for filename, df in inputs.items()
        ]
        return children