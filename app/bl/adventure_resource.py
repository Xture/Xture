from app import mongo
from bson import ObjectId


def create_adventure(*args, **kwargs):
    try:
        kwargs['images']
    except KeyError:
        kwargs['images'] = []
    mongo.db.adventure.insert(kwargs)


def get_adventure_by_id(_id):
    adv = mongo.db.adventure.find_one({'_id': ObjectId(_id)})
    return adv


def get_list_of_adventures():
    ls_ = list(mongo.db.adventure.find())
    return ls_


def get_nearest(lat, lng, min_dist=0, max_dist=1000):
    query = {
        'location': {
            '$near': {
                "$geometry": {"type": "Point", "coordinates": [lat, lng]},
                "$minDistance": min_dist,
                "$maxDistance": max_dist
            }
        }
    }
    places = mongo.db.adventure.find(query)
    return list(places)
