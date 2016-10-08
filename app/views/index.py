from flask import render_template, jsonify

from app import mongo
from app.bl.adventure_resource import get_adventure_by_id


def index_view():
    return render_template('index.html')


def adventure_view(id_):
    # TODO: get adventure by id
    adv = get_adventure_by_id(id_)
    return render_template(
        'view_adventure.html',
        adventure=adv,
    )


def test_post_mongo():
    mongo.db.test.insert_one({"lol": 'lol'})
    return jsonify({})


def test_get_mongo():
    ls_ = list(mongo.db.test.find())
    return jsonify(ls_)
