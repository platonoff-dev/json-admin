import flask
from flask.templating import render_template

import schema


def create_view(s: schema.Schema):
    def view() -> str:
        return render_template("create_template.j2", schema=s)

    return view


def create_item():
    print()
    return flask.Response(status=200)
