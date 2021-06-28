# -*- coding: utf-8 -*-

"""
FAIRifier's user interface
"""

import base64
import io
import datetime
import dash
import dash_table

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State
from collections import OrderedDict


# ------------------------------------------------------------------------------
# Start app
# ------------------------------------------------------------------------------
app_title = 'CORAL portal'
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

# ------------------------------------------------------------------------------
# Input data page
# ------------------------------------------------------------------------------
input_data = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div(['Drag and Drop or ', html.A('Select File')]),
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


def parse_contents(contents, filename, date):

    # Parse filename
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    # Read data
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div(['There was an error processing this file.'])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])


@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'),
              suppress_callback_exceptions=True)
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)
        ]
        return children


# ------------------------------------------------------------------------------
# Annotation page
# ------------------------------------------------------------------------------
df2 = pd.DataFrame(OrderedDict([
    ('climate', ['Sunny', 'Snowy', 'Sunny', 'Rainy']),
    ('temperature', [13, 43, 50, 30]),
    ('city', ['NYC', 'Montreal', 'Miami', 'NYC'])
]))

annotation = html.Div([
    dash_table.DataTable(
        id='table-dropdown',
        data=df2.to_dict('records'),
        columns=[
            {'id': 'climate', 'name': 'climate', 'presentation': 'dropdown'},
            {'id': 'temperature', 'name': 'temperature'},
            {'id': 'city', 'name': 'city', 'presentation': 'dropdown'},
        ],
        editable=True,
        dropdown={
            'climate': {
                'options': [
                    {'label': i, 'value': i}
                    for i in df2['climate'].unique()
                ]
            },
            'city': {
                 'options': [
                    {'label': i, 'value': i}
                    for i in df2['city'].unique()
                ]
            }
        }
    ),
    html.Div(id='table-dropdown-container')
])


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

