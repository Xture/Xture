from flask import request, jsonify
from app import logger
from app.utils import to_json
from app.utils import validate_input
from app.utils import is_authenticated

from app.bl.engagments_resource import create_like
from app.bl.engagments_resource import create_comment


comment_schema = {
    "type": 'object',
    "properties": {
        "text": {"type": 'string'},
    }
}


@to_json
@validate_input(comment_schema)
@is_authenticated
def like_view(id_):
    if request.method == 'POST':
        logger.debug("Trying to put like for post" + str(id_))
        user_id = request.user_id
        create_comment(id_, user_id, request.json['text'])
        return {'status': 'OK'}


@to_json
@is_authenticated
def comment_view(id_):
    if request.method == 'POST':
        logger.debug("Trying to put like for post" + str(id_))
        user_id = request.user_id
        create_like(id_, user_id)
        return {'status': 'OK'}
