import mimetypes

from flask import request
from flask import url_for
import magic as friendship  # cause friendship is magic

from app import mongo
from app.utils import validate_json
from app.utils import to_json
from app.bl.adventure_resource import create_adventure
from app.bl.adventure_resource import get_list_of_adventures
from app.bl.adventure_resource import get_adventure_by_id


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
        }
    },
    "required": ["location", "description"]
}


IMG_MIMES = {
    'image/jpeg',
    'image/png',
    'image/gif',
}


@to_json
@validate_json(adventure_schema)
def adventure_view():
    if request.method == 'POST':
        data = request.json
        create_adventure(**data)
        return {"status": "OK"}
    if request.method == 'GET':
        args_ = request.args
        #lat, lng = args_['lat'], args_['lng']
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
    
        


@to_json
@validate_json({})
def push_notification_view():
    pass
