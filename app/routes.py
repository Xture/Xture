from .views.index import index_view


def setup_routes(app):
    app.add_url_rule('/', 'index', view_func=index_view)
