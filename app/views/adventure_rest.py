import json

from app import logger
from flask import request
from flask import url_for
import magic as friendship  # cause friendship is magic

from app import mongo
from app.utils import validate_input
from app.utils import to_json
from app.utils import is_authenticated
from app.bl.adventure_resource import create_adventure
from app.bl.adventure_resource import get_list_of_adventures
from app.bl.adventure_resource import get_adventure_by_id
from app.bl.adventure_resource import get_nearest


adventure_schema = {
    "type": "object",
    "properties": {
        "description": {'type': "string"},
        "location": {
            'type': "array",
            "items": {
                'type': 'number'
            },
            "maxItems": 2
        },
        'title': {'type': 'string'}
    },
    "required": ["location", "description"]
}

nearest_args = {
    'type': "object",
    "properties": {
        "lat": {'type': 'number'},
        "lng": {'type': 'number'},
    },
    "required": ['lat', 'lng']
}


IMG_MIMES = {
    'image/jpeg',
    'image/png',
    'image/gif',
}


@to_json
@is_authenticated
@validate_input(adventure_schema)
def adventure_view():
    if request.method == 'POST':
        data = request.json
        data['creator'] = str(request.user_id)
        logger.debug('Creating new adv: {}'.format(json.dumps(data)))
        create_adventure(**data)
        return {"status": "OK"}
    if request.method == 'GET':
        data = get_list_of_adventures()
        return data, 200


@to_json
def add_image(adventure_id):
    import gridfs
    from bson import ObjectId

    # TODO: handle possible errors here
    adv = get_adventure_by_id(ObjectId(adventure_id))
    if not adv:
        return {"status": "error"}, 404

    image = request.files['img']
    buf = image.stream.read()
    image.stream.seek(0)
    mime = friendship.from_buffer(buf, mime=True)
    if mime in IMG_MIMES:
        img_id = gridfs.GridFS(mongo.db).put(image)
        images = adv.get('images', [])
        images.append(img_id)
        adv['images'] = images
        return {
            "status": "OK",
            "result": url_for('image', image_id=img_id),
        }
    return (
        {
            "status": "error",
            "reason": "Filetype {} is not allowed".format(mime),
        },
        400,
    )


@is_authenticated
@validate_input(nearest_args, location='args')
def nearest_adventures_view():
    args_ = request.args
    lat, lng = float(args_['lat']), float(args_['lng'])
    return {'nearest': get_nearest(lat, lng)}
