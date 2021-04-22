from flask import Flask
from config import Config

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    with app.app_context():
        from . import routes

        # import and init dash
        from .dashboard import init_dashboard
        app = init_dashboard(app)

        return app