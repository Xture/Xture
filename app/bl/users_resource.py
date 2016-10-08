import uuid
from app import mongo


def get_user_by_social_provider(provider, id_):
    user = mongo.db.users.find_one({'social_{}_id'.format(provider): id_})
    return user


def create_user_by_social_provider(provider, id_, login, *args, **kwargs):
    password = str(uuid.uuid4())
    mongo.db.users.insert({'provider_{}_id'.format(provider): id_, 'password': password, 'login': login})
    return password
