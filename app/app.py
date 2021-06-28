# -*- coding: utf-8 -*-

"""
FAIRifier's user interface
"""

import dash
import dash_table

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from dash.dependencies import Input
from dash.dependencies import Output
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
                dbc.NavItem(dbc.NavLink('Annotations', href='/annotations', active='exact'))
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
# Annotation page
# ------------------------------------------------------------------------------
df = pd.DataFrame(OrderedDict([
    ('climate', ['Sunny', 'Snowy', 'Sunny', 'Rainy']),
    ('temperature', [13, 43, 50, 30]),
    ('city', ['NYC', 'Montreal', 'Miami', 'NYC'])
]))

annotation = html.Div([
    dash_table.DataTable(
        id='table-dropdown',
        data=df.to_dict('records'),
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
                    for i in df['climate'].unique()
                ]
            },
            'city': {
                 'options': [
                    {'label': i, 'value': i}
                    for i in df['city'].unique()
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

