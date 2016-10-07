import os
from flask import Flask

from .routes import setup_routes

def create_app():
    app = Flask(__name__)
    filepath = os.getenv('APP_CONFIG')
    abspath = os.path.abspath(filepath)
    app.config.from_pyfile(abspath)
    setup_routes(app)

    return app