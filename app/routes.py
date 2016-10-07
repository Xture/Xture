from .views.index import index_view
from .views.index import adventure_view


def setup_routes(app):
    app.add_url_rule('/', 'index', view_func=index_view)
    app.add_url_rule('/adventure/<int:id_>', 'adventure_view', view_func=adventure_view)
