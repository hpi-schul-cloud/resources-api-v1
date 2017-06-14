import jsonschema
import os
import json
import sys


HERE = os.path.dirname(__file__)
JSON_PATH = os.path.join(HERE, "json")
NO_SCHEMA = ["test"]

ValidationFailed = jsonschema.exceptions.ValidationError


def _get_json_content_from_folder(folder):
    """yield objects from json files in the folder and subfolders."""
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.lower().endswith(".json"):
                filepath = os.path.join(dirpath, filename)
                with open(filepath, "rb") as file:
                    yield json.loads(file.read().decode("UTF-8"))


class Schema(object):
    """An interface to the schema on the file system."""

    def __init__(self, name):
        """Create a schema with a given name."""
        self._name = name

    def _get_schema_folder(self):
        """Return the path to the schema folder where all files are located."""
        return os.path.join(JSON_PATH, self._name)

    def get_schema(self):
        """Return the schema."""
        path = os.path.join(self._get_schema_folder(), self._name + ".json")
        with open(path, "rb") as file:
            schema = json.loads(file.read().decode("UTF-8"))
        if sys.platform.lower().startswith("win") and len(path) >= 2 and path[1] == ":":
            path = path[2:].replace("\\", "/")
        schema["id"] = "file://" + path
        return schema

    def validate(self, object):
        """Validate an object against the schema.

        This function just passes if the schema matches the object.
        If the object does not match the schema, a ValidationException is raised.
        This error allows debugging.
        """
        jsonschema.validate(object, self.get_schema())

    def is_valid(self, object):
        """Return whether an object matches the schema."""
        try:
            self.validate(object)
        except ValidationFailed:
            return False
        return True

    def get_valid_examples(self):
        """Return a list of valid examples for the given schema."""
        path = os.path.join(self._get_schema_folder(), "examples", "valid")
        return list(_get_json_content_from_folder(path))

    def get_invalid_examples(self):
        """Return a list of examples which violate the schema."""
        path = os.path.join(self._get_schema_folder(), "examples", "invalid")
        return list(_get_json_content_from_folder(path))


def get_schemas():
    """Return a dict of schema names mapping to a Schema.

    The schema is of type schul_cloud_resources_api_v1.schema.Schema
    """
    schemas = {}
    for name in os.listdir(JSON_PATH):
        if name not in NO_SCHEMA:
            schemas[name] = Schema(name)
    return schemas


_resource_schema = get_schemas()["resource"]
get_resource_schema = _resource_schema.get_schema
validate_resource = _resource_schema.validate
is_valid_resource = _resource_schema.is_valid
get_valid_examples = _resource_schema.get_valid_examples
get_invalid_examples = _resource_schema.get_invalid_examples


__all__ = ["ValidationFailed", "validate_resource", "is_valid_resource",
           "get_valid_examples", "get_invalid_examples", "get_schemas",
           "Schema"]
