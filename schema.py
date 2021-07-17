from typing import List

import flask


class ValidationError(Exception):
    def __init__(self, message: str, *args: object) -> None:
        super().__init__(*args)
        self.message = message


def _validate_field(field: dict, field_idx: int):
    if not isinstance(field, dict):
        raise ValidationError(f"Field {field_idx} is not dict")

    allowed_types = ["text"]
    required_fields = {
        "name": str,
        "type": str
    }

    for name, t in required_fields.items():
        if name not in field:
            raise ValidationError(f"`{name}` not found in field {field_idx}")
        if not isinstance(field[name], t):
            raise ValidationError(f"`{name}` has invalid type. Must be {t}, has {type(field[name])}. Field: {field_idx}")
    
    if field[name] not in allowed_types:
        raise ValidationError(f"Field type not allowed. Field: {field_idx}")
        
    


def validate(schema: dict) -> None:
    if "fields" not in schema:
        raise ValidationError("`field` field not found in schema declaration")
    
    if "meta" not in schema:
        raise ValidationError("`meta` field not found in schema declaration")

    fields = schema["fields"]
    if not isinstance(fields, list) :
        raise ValidationError("`fields` must be list of dicts")
    if len(fields) == 0:
        raise ValidationError("`fields` must be not empty")

    meta = schema["meta"]
    if not isinstance(meta, dict):
        raise ValidationError("`meta` must be a dict")
    
    for i, field in enumerate(fields):
        _validate_field(field, i)


def generate_create_view(schema: dict):
    def view():
        return flask.render_template("create_template.j2", schema=schema)

    return view

def generate_update_view(schema: dict):
    pass

def generate_list_view(schema: dict):
    pass


class Field:
    name: str
    field_type: str


class Meta:
    pass


class Schema:
    _meta: Meta
    _fields: List[Field]

    def __init__(self) -> None:
        pass
