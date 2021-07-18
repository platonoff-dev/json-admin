# json-admin
Json based for generator


### Json format
```json
{
    meta: {
        "list_fields": ["field_1", "field_2", "field_2"],
        "allow_delete": true,
        "allow_update": true,
    }
    fields: [
        {
            "name": "field_name", // Name of field
            "type": "field_type", // Field type like in forms input 
            "default": "default_value",
            "read_only": false,
            "disabled": false,
            "max_length": "10", // Maximum length of allowed value,
            "min": "0",
            "max": "0",
            "multiple": true,
            "pattern": "[A-Za-z]{3}",
            "placeholder": "123-4565-789",
            "required": true,
            "list": ["1", "2", "3"]
        }
    ]
}
```

For type used html input types: 
button, checkbox, color, date, datetime-local, email, file, hidden, image, month, number, password, radio, range, reset, search, submit, tel, text, time, url, week


### Possible errors
```json
{
    "error": "Validation error. Bad schema format",
    "payload": {}
}
```
