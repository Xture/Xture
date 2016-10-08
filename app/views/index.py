from flask import render_template, jsonify
from flask import current_app as app
from flask import request
from ..utils import objectid_fix
from ..business_logic.adventure_resource import get_adventure_by_id, create_adventure

def index_view():
    return render_template('index.html')


def adventure_view(id_):
    # TODO: get adventure by id
    adv = get_adventure_by_id(id_)
    return render_template(
        'view_adventure.html',
        adventure=adv,
    )

def create_adventure_view():
    input_data = request.form
    try:
        create_adventure(**input_data)
    except:
        return jsonify({}), 400


def test_post_mongo():
    app.db.test.insert_one({"lol": 'lol'})
    return jsonify({})


def test_get_mongo():
    ls_ = objectid_fix(list(app.db.test.find()))
    return jsonify(ls_)
