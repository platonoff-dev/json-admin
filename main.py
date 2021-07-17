from flask import Flask
import json

import schema


def welcome_view() -> str:
    return "Welcome to json admin generator!!!"

def read_schema() -> dict:
    with open("schema.json", "r") as json_file:
        return json.load(json_file)


def main() -> None:
    app = Flask(__name__)

    settins = read_schema()
    schema.validate(settins)

    app.add_url_rule("/create", view_func=schema.generate_create_view(settins))

    app.run(port=8088)


if __name__ == "__main__":
    main()
