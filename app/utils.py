from flask import request, jsonify
from jsonschema import (
    validate,
    ValidationError
)
from functools import wraps
import json
from app import cache
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o.decode('utf-8'))


def is_authenticated(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return {'message': 'No authorization provided'}, 401
        token = request.headers['Authorization']

        user_id = cache.get(token)
        print(user_id)
        if user_id:
            setattr(request, 'user_id', str(user_id.decode('utf-8')))
            return func(*args, **kwargs)
        else:
            return {'message': 'token is missing or expired'}, 403
    return wrapper


def validate_input(format_, location='json'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.method != 'POST':
                return func(*args, **kwargs)
            data = getattr(request, location)
            try:
                validate(data, format_)
                return func(*args, **kwargs)
            except ValidationError as error:
                return {'message': error.message}
        return wrapper
    return decorator


def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        returned = func(*args, **kwargs)
        print(returned)
        if isinstance(returned, tuple):
            returned, status_code = returned
            return jsonify(returned), status_code
        else:
            return jsonify(returned)
    return wrapper
