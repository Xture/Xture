import os

from flask import Flask
from flask_script import Manager
from flask_pymongo import PyMongo


app = Flask(__name__, static_folder='../static')
manager = Manager(app)
filepath = os.getenv('APP_CONFIG')

abspath = os.path.abspath(filepath)
app.config.from_pyfile(abspath)

# mongodb setup
mongo = PyMongo(app)

from app.routes import setup_routes
from app.routes import RegexConverter
app.url_map.converters['regex'] = RegexConverter
setup_routes(app)
