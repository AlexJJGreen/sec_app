from dash import Dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html

def init_dashboard(server):
    """create dashboard instance"""
    dash_app = Dash(
        server=server,
        routes_pathname_prefix="/dashboard/",
        external_stylesheets=['/static/dist/css/styles.css',
        ]
    )

    #dash layout
    dash_app.layout = html.Div(id="dash-container")

    return dash_app.server