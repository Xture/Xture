from flask import request
from app.utils import validate_json
from app.utils import to_json
from app.bl.adventure_resource import create_adventure
from app.bl.adventure_resource import get_list_of_adventures

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
@validate_json({})
def push_notification_view():
    pass
