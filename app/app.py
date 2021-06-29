# -*- coding: utf-8 -*-

"""
FAIRifier's user interface
"""

import base64
import io
import dash
import dash_table

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State


# ------------------------------------------------------------------------------
# Start app
# ------------------------------------------------------------------------------
app_title = 'CORAL portal'
inputs = None
children = None
#app = dash.Dash(external_stylesheets=[dbc.themes.MINTY])
app = dash.Dash(__name__)

# ------------------------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------------------------
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '16rem',
    'padding': '2rem 1rem',
    'background-color': '#f8f9fa',
}

sidebar = html.Div(
    [
        html.H2(app_title, className='display-8'),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink('Home', href='/', active='exact')),
                dbc.NavItem(dbc.NavLink('Input', href='/input',
                                        active='exact')),
                dbc.NavItem(dbc.NavLink('Annotations', href='/annotations',
                                        active='exact'))
            ],
            vertical='md',
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

# ------------------------------------------------------------------------------
# Content
# ------------------------------------------------------------------------------
CONTENT_STYLE = {
    'margin-left': '18rem',
    'margin-right': '2rem',
    'padding': '2rem 1rem',
}

content = html.Div(id='page-content', style=CONTENT_STYLE)

# ------------------------------------------------------------------------------
# Layout
# ------------------------------------------------------------------------------
app.layout = html.Div([dcc.Location(id='url'), sidebar, content])
app.config.suppress_callback_exceptions = True

# ------------------------------------------------------------------------------
# Input data page
# ------------------------------------------------------------------------------
input_data = html.Div([
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
        return html.Div(['Not able to parse the file: %s' % filename])
    else:
        return html.Div([
            html.H5('Uploaded file: %s' % filename),
            dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df.columns]
            )
        ])


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


#@app.callback(Output('output-data-upload', 'children'),
#              Input('input-data', 'data'))
#def update_display_data(data):
#    global inputs
#    if inputs is not None:
#        children = [
#            display_data(filename, df) for filename, df in inputs.items()
#        ]
#        return children


# ------------------------------------------------------------------------------
# Annotation page
# ------------------------------------------------------------------------------
annotation = html.Div([
    html.P('Terminology mapping'),
    dbc.DropdownMenu(
        id='input-filename',
        label='Select a file:',
        children=[
            dbc.DropdownMenuItem('Test1'),
            dbc.DropdownMenuItem('Test2')
        ],
    ),
    html.Div(id='output-annotation'),
])


@app.callback(Output('output-annotation', 'children'),
              Input('input-filename', 'value'))
def update_annotations(filename):
    # TODO: implement multiple files option
    if inputs is not None:
        df = inputs[list(inputs.keys())[0]]

        return html.Div([
            dash_table.DataTable(
                id='table-dropdown',
                data=df.to_dict('records'),
                columns=[
                    {'id': i, 'name': i, 'presentation': 'dropdown'}
                    for i in df.columns
                ],
                editable=True,
                dropdown={
                    j: {
                        'options': [
                            {'label': i, 'value': i} for i in df[j].unique()
                        ]
                    } for j in df.columns
                }
            ),
            html.Div(id='table-dropdown-container')
        ])
    else:
        return html.P('Please upload a file!')


# ------------------------------------------------------------------------------
# Render page
# ------------------------------------------------------------------------------
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page_content(pathname):
    if pathname == '/':
        return html.P('Welcome to the CORAL portal!')
    elif pathname == '/input':
        return input_data
    elif pathname == '/annotations':
        return annotation
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1('404: Not found', className='text-danger'),
            html.Hr(),
            html.P(f'The address {pathname} was not recognised...'),
        ]
    )


# ------------------------------------------------------------------------------
# Run app
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, port=5050)

