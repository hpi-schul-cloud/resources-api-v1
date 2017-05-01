"""This module handles the global authentication.

Authentication is a global state.
When authenticating make sure to encrypt the connection.
All credentials can be read.
"""

def none():
    """Delete all authentication.

    This is the default case.
    """

    
def basic(username, password):
    """Add basic authentication to the requests of the clients."""


def api_key(api_key):
    """Authenticate via an api key."""



__all__ = ["none", "basic", "api_key"]