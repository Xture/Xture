import os
from flask import Flask, current_app
from flask_pymongo import PyMongo

from .routes import setup_routes

def connection(mongo):
    def _():
        setattr(current_app, 'db', mongo.db)
    return _

def create_app():
    app = Flask(__name__)
    app.config['MONGO_DBNAME'] = 'xture'
    mongo = PyMongo(app)

    app.before_request(connection(mongo))

    filepath = os.getenv('APP_CONFIG')
    abspath = os.path.abspath(filepath)
    app.config.from_pyfile(abspath)
    setup_routes(app)

    return app
