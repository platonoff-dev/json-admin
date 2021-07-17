from flask import Flask
import json

import flask

import schema
import views


def welcome_view() -> str:
    return "Welcome to json admin generator!!!"

def read_schema() -> dict:
    with open("schema.json", "r") as json_file:
        return json.load(json_file)

def main() -> None:
    app = Flask(__name__)

    s = schema.Schema(read_schema())
    app.add_url_rule("/create/", view_func=views.create_view(s))
    app.add_url_rule("/list/", view_func=views.list_view(s))
    app.add_url_rule("/item/", view_func=views.create_item, methods=["POST"])

    app.run(port=8088)


if __name__ == "__main__":
    main()
