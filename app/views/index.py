from flask import render_template


def index_view():
    return render_template('index.html')


def adventure_view(id_):
    # TODO: get adventure by id
    return render_template(
        'view_adventure.html',
        adventure_id=id_,
    )
