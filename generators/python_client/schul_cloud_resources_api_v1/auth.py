"""This module handles the global authentication.

Authentication is a global state.
When authenticating make sure to encrypt the connection.
All credentials can be read.
"""

from __future__ import absolute_import

from .configuration import Configuration
from base64 import b64encode


_config = Configuration()

def none():
    """Delete all authentication.

    This is the default case.
    """
    _config.username = None
    _config.password = None
    _config.api_key_prefix = {}
    _config.api_key = {}


def basic(username, password):
    """Add basic authentication to the requests of the clients."""
    none()
    _config.username = username
    _config.password = password


def api_key(api_key):
    """Authenticate via an api key."""
    none()
    _config.api_key_prefix["Authorization"] = "api-key"
    _config.api_key["Authorization"] = "key=" + b64encode(api_key.encode()).decode()

none()

__all__ = ["none", "basic", "api_key"]
