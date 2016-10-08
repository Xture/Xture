import uuid

from app import mongo
from app import cache

from app.utils import validate_input
from app.utils import to_json
from flask import request

login_validation = {
    'type': 'object',
    'properties': {
        'login': {'type': 'string'},
        'password': {'type': 'string'}
    },
    'required': ['login', 'password']
}

signup_validation = {
    'type': 'object',
    'properties': {
        'login': {'type': 'string'},
        'password': {'type': 'string'},
        'confirm': {'type': 'string'}
    },
    'required': ['login', 'password']
}


@to_json
@validate_input(login_validation)
def login_view():
    data = request.json
    user = mongo.db.users.find_one(data)
    if user:
        token = str(uuid.uuid4())
        cache.set(token, user['_id'], ex=86400)
        return {'token': token}
    else:
        return {"message": 'You are not authorized'}


@to_json
@validate_input(signup_validation)
def signup_view():
    data = request.json
    if data['confirm'] == data['password']:
        mongo.db.users.insert(data)
        return {'status': 'OK'}
    else:
        return {'message': 'Password and config password do not match'}, 401
