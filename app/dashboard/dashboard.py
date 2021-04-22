from dash import Dash

def init_dashboard(server):
    """create dashboard instance"""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/dashboard/",
        external_stylesheets=['/static/dist/css/styles.css',
        ]
    )

    #dash layout
    dash_app.layout = html.Div(id="dash-container")

    return dash_app.server