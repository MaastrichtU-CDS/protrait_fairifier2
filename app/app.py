# -*- coding: utf-8 -*-

"""
FAIRifier's app
"""

import dash


app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server