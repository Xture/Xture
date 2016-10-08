from app import mongo
from app.utils import objectid_fix


def create_adventure(*args, **kwargs):
    mongo.db.xture.insert(**kwargs)


def get_adventure_by_id(_id):
    adv = mongo.db.xture.find_one({'_id': _id})
    return objectid_fix(adv)


def get_list_of_adventures():
    ls_ = list(mongo.db.xture.find_all())
    return objectid_fix(ls_)
