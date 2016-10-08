import uuid

from app import mongo
from app import logger
from app import cache

from app.utils import validate_input
from app.utils import to_json
from app.bl.users_resource import get_user_by_social_provider, create_user_by_social_provider
from app.views.social_integrations import vk_signup, get_profile_data
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

vk_code = {
    'type': 'object',
    'properties': {
        'code': {'type': 'string'},
    },
    'required': ['code']
}


@to_json
@validate_input(login_validation)
def login_view():
    data = request.json
    user = mongo.db.users.find_one(data)
    if user:
        token = str(uuid.uuid4())
        cache.set(token, str(user['_id']), ex=86400)
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


@validate_input(vk_code)
def vk_auth_view():
    data = request.args
    token, vk_uid = vk_signup(data['code'])
    profile = get_profile_data(token, vk_uid)
    user = get_user_by_social_provider('vk', vk_uid)
    login = '{} {}'.format(profile['first_name'], profile['last_name'])
    x_token = str(uuid.uuid4())
    if not user:
        logger.debug('new user')
        password = create_user_by_social_provider('vk', vk_uid, login)
        data = {'password': password, 'login': login}
        user = mongo.db.users.find_one(data)
        cache.set(x_token, str(user['_id']), ex=86400)
    else:
        logger.debug('old user')
        cache.set(x_token, str(user['_id']), ex=86400)
    return "<script>\nwindow.opener.localStorage.setItem('token','{}'); window.opener.location='/adventures/new';window.close()\n</script>".format(x_token)
