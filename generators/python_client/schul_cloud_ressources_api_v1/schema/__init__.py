import jsonschema


class ValidationFailed(jsonschema.exceptions.ValidationError):
    """Schema validation failed."""



def validate_ressource(ressource):
    """Validate the schema of a ressource.
    
    This function just passes if the schema matches the ressource.
    If the ressource does not fit, an ValidationFailed is raised.
    """

def is_valid_ressource(ressource):
    """Return whether a the given ressources fits into the schema."""


def get_valid_examples():
    """Return a list of json objects that are valid examples for ressources."""
    return [""]


def get_invalid_examples():
    """Return a list of json objects that are invalid examples for ressources."""
    return [""]
