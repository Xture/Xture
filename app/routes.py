from werkzeug.routing import BaseConverter
from app.views.index import (
    index_view,
    test_post_mongo,
    test_get_mongo,
    adventure_view,
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
        '/adventure/<regex("[0-9a-fA-F]{24}"):id_>',
        'adventure_view',
        view_func=adventure_view,
    )
    app.add_url_rule(
        '/test', 'get',
        view_func=test_get_mongo,
    )
    app.add_url_rule(
        '/test/post', 'post',
        view_func=test_post_mongo,
        methods=['POST'],
    )
