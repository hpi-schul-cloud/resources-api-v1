import jsonschema
import os
import json
import sys


HERE = os.path.dirname(__file__)
VALID_SCHEMAS_PATH = os.path.join(HERE, "json/resource/examples/valid/")
INVALID_SCHEMAS_PATH = os.path.join(HERE, "json/resource/examples/invalid/")
JSON_SCHEMA_PATH = os.path.join(HERE, "json/resource/resource.json")


ValidationFailed = jsonschema.exceptions.ValidationError


def get_resource_schema():
    """Return the json schema for the resource."""
    with open(JSON_SCHEMA_PATH, "rb") as file:
        schema = json.loads(file.read().decode("UTF-8"))
    path = JSON_SCHEMA_PATH
    if sys.platform.lower().startswith("win") and len(path) >= 2 and path[1] == ":":
        path = path[2:].replace("\\", "/")
    schema["id"] = "file://" + path
    return schema


def validate_resource(resource):
    """Validate the schema of a resource.
    
    This function just passes if the schema matches the resource.
    If the resource does not fit, an ValidationFailed is raised.
    """
    jsonschema.validate(resource, get_resource_schema())


def is_valid_resource(resource):
    """Return whether a the given resources fits into the schema."""
    try:
        validate_resource(resource)
    except ValidationFailed:
        return False
    return True


def _get_json_content_from_folder(folder):
    """yield objects from json files in the folder and subfolders."""
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.lower().endswith(".json"):
                filepath = os.path.join(dirpath, filename)
                with open(filepath, "rb") as file:
                    yield json.loads(file.read().decode("UTF-8"))


def get_valid_examples():
    """Return a list of json objects that are valid examples for resources."""
    return list(_get_json_content_from_folder(VALID_SCHEMAS_PATH))


def get_invalid_examples():
    """Return a list of json objects that are invalid examples for resources."""
    return list(_get_json_content_from_folder(INVALID_SCHEMAS_PATH))


__all__ = ["ValidationFailed", "validate_resource", "is_valid_resource",
           "get_valid_examples", "get_invalid_examples"]
