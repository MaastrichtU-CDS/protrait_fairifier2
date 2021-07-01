# -*- coding: utf-8 -*-

"""
FAIRifier's app
"""

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input
from dash.dependencies import Output

from app import app
from pages import home
from pages import input_data
from pages import annotations


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
        html.H1('FAIRifier', className='display-8'),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink('Home', href='/', active='exact')),
                dbc.NavItem(dbc.NavLink('Data', href='/input_data',
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
# Page content
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
app.layout = html.Div([dcc.Location(id='url', refresh=False), sidebar, content])


# ------------------------------------------------------------------------------
# Render page
# ------------------------------------------------------------------------------
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page_content(pathname):
    if pathname == '/':
        return home.layout
    elif pathname == '/input_data':
        return input_data.layout
    elif pathname == '/annotations':
        return annotations.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron([
        html.H1('404: Not found', className='text-danger'),
        html.Hr(),
        html.P(f'The address {pathname} was not recognised...'),
    ])


# ------------------------------------------------------------------------------
# Run app
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, port=5050)