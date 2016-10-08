from flask import abort
from flask import jsonify
from flask import render_template
from flask import make_response

import magic as friendship

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


def image_view(image_id):
    import gridfs
    from bson import ObjectId
    id_ = ObjectId(image_id)
    grid_fs = gridfs.GridFS(mongo.db)
    if grid_fs.exists(id_):
        image_stream = grid_fs.get(id_)
        buf = image_stream.read()
        response = make_response(buf)
        mime = friendship.from_buffer(buf, mime=True)
        response.mimetype = mime
        return response
    abort(404)


def test_post_mongo():
    mongo.db.test.insert_one({"lol": 'lol'})
    return jsonify({})


def test_get_mongo():
    ls_ = list(mongo.db.test.find())
    return jsonify(ls_)
