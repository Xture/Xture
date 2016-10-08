from flask import current_app as app
from ..utils import objectid_fix


def create_adventure(*args, **kwargs):
    app.db.xture.insert(**kwargs)


def get_adventure_by_id(_id):
    adv = app.db.xture.find_one({'_id': _id})
    return objectid_fix(adv)


def get_list_of_adventures():
    ls_ = list(app.db.xture.find_all())
    return objectid_fix(ls_)
