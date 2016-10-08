from werkzeug.routing import BaseConverter
from app.views.index import index_view

from app.views.index import adventure_view as single_adventure_view
from app.views.index import image_view
from app.views.index import login_view as static_login_view

from app.views.index import adventure_add_view
from app.views.index import nearest_adventures
from app.views.adventure_rest import adventure_view
from app.views.adventure_rest import nearest_adventures_view

from app.views.adventure_rest import add_image

from app.views.auth_rest import signup_view
from app.views.auth_rest import login_view
from app.views.auth_rest import vk_auth_view

from app.views.engagements_rest import like_view


# Based on http://stackoverflow.com/a/5872904
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


def setup_routes(app):
    app.add_url_rule(
        '/', 'index',
        view_func=index_view
    )
    app.add_url_rule(
        '/api/adventure/',
        'create_adventure_view',
        methods=['POST', 'GET'],
        view_func=adventure_view,
    )
    app.add_url_rule(
        '/api/adventure/nearest/',
        'nearest_adventures_view',
        view_func=nearest_adventures_view,
    )
    app.add_url_rule(
        '/adventure/nearest_adventures/',
        'nearest_adventures',
        view_func=nearest_adventures,
    )

    app.add_url_rule(
        '/login',
        'login_static_page',
        view_func=static_login_view,
    )

    app.add_url_rule(
        '/adventure/new',
        'adventure_add_view',
        view_func=adventure_add_view,
    )

    app.add_url_rule(
        '/api/adventure/<regex("[0-9a-fA-F]{24}"):id_>',
        'adventure_view',
        view_func=single_adventure_view,
    )
    app.add_url_rule(
        '/adventure/<regex("[0-9a-fA-F]{24}"):adventure_id>/add_image',
        'adventure_image_uploader',
        methods=['POST'],
        view_func=add_image,
    )
    app.add_url_rule(
        '/image/<regex("[0-9a-fA-F]{24}"):image_id>',
        'image',
        view_func=image_view,
    )
    app.add_url_rule(
        '/api/adventure/<regex("[0-9a-fA-F]{24}"):id_>/likes',
        'adv_likes',
        methods=['POST'],
        view_func=like_view,
    )
    # auth handlers
    app.add_url_rule(
        '/api/auth/signup',
        'signup',
        view_func=signup_view,
        methods=['POST']
    )
    app.add_url_rule(
        '/api/auth/login',
        'login',
        view_func=login_view,
        methods=['POST']
    )
    app.add_url_rule(
        '/api/auth/vk',
        'vk_signup',
        view_func=vk_auth_view,
    )
