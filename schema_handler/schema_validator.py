import json
import logging
import sys

from utils.constants import DATA_TYPES


class DataTypeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def validate_and_read_json_as_object(json_schema: str):
    try:
        json_object = json.loads(json_schema)
        schema_dict = json_object["properties"]
        for column_name in schema_dict:
            type_dict = schema_dict[column_name]
            data_type = type_dict["type"].upper()
            if data_type not in DATA_TYPES:
                raise (DataTypeError(data_type))

    except ValueError as ex:
        logging.error(f"Invalid json schema file provided: {ex}")
        return SyntaxError

    except DataTypeError as ex:
        logging.error(
            f"Invalid data type {ex.value} detected in json. Supported data type {DATA_TYPES}"
        )
        sys.exit(1)

    return json_object
