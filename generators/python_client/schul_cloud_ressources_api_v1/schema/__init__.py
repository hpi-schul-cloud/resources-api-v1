import jsonschema
import os
import json


HERE = os.path.dirname(__file__)
VALID_SCHEMAS_PATH = os.path.join(HERE, "ressource/examples/valid/")
INVALID_SCHEMAS_PATH = os.path.join(HERE, "ressource/examples/invalid/")


class ValidationFailed(jsonschema.exceptions.ValidationError):
    """Schema validation failed."""



def validate_ressource(ressource):
    """Validate the schema of a ressource.
    
    This function just passes if the schema matches the ressource.
    If the ressource does not fit, an ValidationFailed is raised.
    """

def is_valid_ressource(ressource):
    """Return whether a the given ressources fits into the schema."""


def _get_json_content_from_folder(folder):
    """yield objects from json files in the folder and subfolders."""
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.lower().endswith(".json"):
                filepath = os.path.join(dirpath, filename)
                with open(filepath, encoding="UTF-8") as file:
                    yield json.load(file)


def get_valid_examples():
    """Return a list of json objects that are valid examples for ressources."""
    return list(_get_json_content_from_folder(VALID_SCHEMAS_PATH))


def get_invalid_examples():
    """Return a list of json objects that are invalid examples for ressources."""
    return list(_get_json_content_from_folder(INVALID_SCHEMAS_PATH))
