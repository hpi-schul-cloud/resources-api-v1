import jsonschema
import os
import json


HERE = os.path.dirname(__file__)
VALID_SCHEMAS_PATH = os.path.join(HERE, "json/ressource/examples/valid/")
INVALID_SCHEMAS_PATH = os.path.join(HERE, "json/ressource/examples/invalid/")
JSON_SCHEMA_PATH = os.path.join(HERE, "json/ressource/ressource.json")


ValidationFailed = jsonschema.exceptions.ValidationError


def get_ressource_schema():
    """Return the json schema for the ressource."""
    with open(JSON_SCHEMA_PATH, "rb") as file:
        schema = json.loads(file.read().decode("UTF-8"))
    schema["id"] = "file://" + JSON_SCHEMA_PATH
    return schema


def validate_ressource(ressource):
    """Validate the schema of a ressource.
    
    This function just passes if the schema matches the ressource.
    If the ressource does not fit, an ValidationFailed is raised.
    """
    jsonschema.validate(ressource, get_ressource_schema())


def is_valid_ressource(ressource):
    """Return whether a the given ressources fits into the schema."""
    try:
        validate_ressource(ressource)
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
    """Return a list of json objects that are valid examples for ressources."""
    return list(_get_json_content_from_folder(VALID_SCHEMAS_PATH))


def get_invalid_examples():
    """Return a list of json objects that are invalid examples for ressources."""
    return list(_get_json_content_from_folder(INVALID_SCHEMAS_PATH))


__all__ = ["ValidationFailed", "validate_ressource", "is_valid_ressource",
           "get_valid_examples", "get_invalid_examples"]
