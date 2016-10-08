import os
import sys
import logging
import redis
from flask import Flask
from flask_script import Manager
from flask_pymongo import PyMongo


app = Flask(__name__, static_folder='../static')
manager = Manager(app)
filepath = os.getenv('APP_CONFIG')
cache = redis.StrictRedis(host='localhost', port=6380, db=0)
abspath = os.path.abspath(filepath)
app.config.from_pyfile(abspath)

# set up custom json encoder to serialize/deserialize
# ObjectID properly
from app.utils import JSONEncoder
app.json_encoder = JSONEncoder

# mongodb setup
mongo = PyMongo(app)

# Configuring logging
formatter = logging.Formatter("[%(name)s][%(levelname)s] %(filename)s:%(lineno)d - %(message)s")
logger = logging.getLogger('user-interaction')
handler = logging.StreamHandler(stream=sys.stderr)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

from app.routes import setup_routes
from app.routes import RegexConverter
app.url_map.converters['regex'] = RegexConverter
setup_routes(app)
