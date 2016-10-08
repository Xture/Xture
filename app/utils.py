from flask import request, jsonify
from jsonschema import (
    validate,
    ValidationError
)
from functools import wraps
import json
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def validate_json(format_):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.method != 'POST':
                return func(*args, **kwargs)
            data = request.json
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
