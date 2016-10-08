from werkzeug.routing import BaseConverter
from app.views.index import index_view
from app.views.index import adventure_view as single_adventure_view

from app.views.adventure_rest import (
    adventure_view,
    nearest_adventures_view
)
from app.views.auth_rest import (
    signup_view,
    login_view
)
from app.views.engagements_rest import (
    like_view,
    comment_view
)

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
        '/adventure/',
        'create_adventure_view',
        methods=['POST', 'GET'],
        view_func=adventure_view,
    )
    app.add_url_rule(
        '/adventure/nearest/',
        'nearest_adventures',
        view_func=nearest_adventures_view,
    )

    app.add_url_rule(
        '/adventure/<regex("[0-9a-fA-F]{24}"):id_>',
        'adventure_view',
        view_func=single_adventure_view,
    )
    app.add_url_rule(
        '/adventure/<regex("[0-9a-fA-F]{24}"):id_>/likes',
        'adv_likes',
        methods=['POST'],
        view_func=like_view,
    )
    app.add_url_rule(
        '/adventure/<regex("[0-9a-fA-F]{24}"):id_>/comments',
        'adv_comments',
        methods=['POST'],
        view_func=comment_view,
    )
    app.add_url_rule(
        '/auth/signup',
        'signup',
        view_func=signup_view,
        methods=['POST']
    )
    app.add_url_rule(
        '/auth/login',
        'login',
        view_func=login_view,
        methods=['POST']
    )
