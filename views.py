from flask import request, Blueprint, current_app

import schema

bp = Blueprint("main", __name__)

@bp.route("/schema/", methods=["POST"])
def load_schema() -> None:
    request_schema = request.get_json()
    schema.validate(request_schema)

    create_view = schema.generate_create_view(schema)
    current_app.add_url_rule("/create", view_func=create_view)

    current_app.res

    return {
        "result": "Read successfully",
        "endpoints": [
            {
                "action": "Create",
                "url": "/create"
            }
        ]
    }