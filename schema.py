from typing import Any, List
from dataclasses import dataclass

import flask


class ValidationError(Exception):
    def __init__(self, message: str, *args: object) -> None:
        super().__init__(*args)
        self.message = message


class Field:    
    name: str
    type: str
    default: Any
    read_only: bool
    disabled: bool
    max_length: int
    min: Any
    max: Any
    multiple: bool
    pattern: str
    placeholder: str
    required: bool
    list: List[str]

    def __init__(self, field: dict) -> None:
        if "name" not in field:
            raise ValidationError("`name` required for field")
        self.name = field["name"].replace(" ", "_").lower()
        self.type = field.get("type", "text")
        self.default = field.get("default", None)
        self.read_only = field.get("read_only", False)
        self.disabled = field.get("disabled", False)

        self.max_length = field.get("max_length", None)
        self.min = field.get("min", None)
        self.max = field.get("max", None)
        self.multiple = field.get("multiple", False)
        self.pattern = field.get("pattern", None)
        self.placeholder = field.get("placeholder", None)
        self.required = field.get("required", False)
        self.list = field.get("list", None)
    

class Meta:
    allow_delete: bool
    allow_update: bool
    list_fields: List[str]

    def __init__(self, meta: dict) -> None:
        self.allow_delete = meta.get("allow_delete")
        self.allow_update = meta.get("allow_update")
        self.list_fields = meta.get("list_fields")


class Schema:
    meta: Meta
    fields: List[Field]

    def __init__(self, schema: dict) -> None:
        if "fields" not in schema:
            raise ValidationError("`field` field not found in schema declaration")
    
        if "meta" not in schema:
            raise ValidationError("`meta` field not found in schema declaration")
        
        fields = schema["fields"]
        if not isinstance(fields, list) :
            raise ValidationError("`fields` must be list of dicts")
        if len(fields) == 0:
            raise ValidationError("`fields` must be not empty")


        self.meta = Meta(schema["meta"])
        self.fields = [Field(f) for f in schema["fields"]]
