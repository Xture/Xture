from flask import render_template, jsonify
from flask import current_app as app
from ..utils import objectid_fix

def index_view():
    return render_template('index.html')


def adventure_view(id_):
    # TODO: get adventure by id
    return render_template(
        'view_adventure.html',
        adventure_id=id_,
    )


def test_post_mongo():
    app.db.test.insert_one({"lol": 'lol'})
    return jsonify({})


def test_get_mongo():
    ls_ = objectid_fix(list(app.db.test.find()))
    return jsonify(ls_)
