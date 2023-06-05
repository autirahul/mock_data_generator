import json

from schema_handler.schema_validator import validate_and_read_json_as_object


def test_schema_validator_for_valid_json():
    json_schema = """{
    "type" : "object",
    "properties" :
        {
        "price" : {"type" : "number"},
        "name" : {"type" : "string"}
        }
        }
    """
    result = validate_and_read_json_as_object(json_schema=json_schema)
    assert result == json.loads(json_schema)


def test_schema_validator_for_invalid_json():
    json_schema = """{
    "type" : "object",
    "properties" : {
        "price" : {"type" : "number"},
        "name" : {"type" : "string"},
        }
        }
    """
    result = validate_and_read_json_as_object(json_schema=json_schema)
    assert result == SyntaxError
