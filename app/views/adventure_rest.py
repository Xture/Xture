from flask import request, jsonify
from app.utils import validate_json, to_json
from app.business_logic.adventure_resource import create_adventure, get_list_of_adventures

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
    }
}


@to_json
@validate_json(adventure_schema)
def adventure_view():
    if request.method == 'POST':
        data = request.json
        create_adventure(**data)
        return {}
    if request.method == 'GET':
        data = get_list_of_adventures()
        return data, 200
