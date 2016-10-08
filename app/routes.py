from .views.index import adventure_view
from .views.index import index_view, test_post_mongo, test_get_mongo


def setup_routes(app):
    app.add_url_rule('/', 'index', view_func=index_view)
    app.add_url_rule('/adventure/<int:id_>', 'adventure_view', view_func=adventure_view)
    app.add_url_rule('/test', 'get', view_func=test_get_mongo)
    app.add_url_rule('/test/post', 'post', view_func=test_post_mongo, methods=['POST'])
