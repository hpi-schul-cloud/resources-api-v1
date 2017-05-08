# coding: utf-8

"""
Tests for schul_cloud_resources_api_v1.auth
"""


from __future__ import absolute_import

import os
import sys
import unittest
import base64


import schul_cloud_resources_api_v1.auth as auth
from schul_cloud_resources_api_v1.configuration import Configuration


class TestAuthentication(unittest.TestCase):
    """Test the authentication mechanism."""
    
    def setUp(self):
        """Create the default state.

        We have global state so we want to remove the side effects.
        """
        auth.none()
        self.config = Configuration()
    tearDown = setUp

    def test_no_authentication_has_no_user_name_and_password(self):
        """By default there is no username and poassword supplied."""
        self.assertFalse(self.config.username)
        self.assertFalse(self.config.password)

    def test_no_authentication_has_no_api_key(self):
        """"By default, the api key is not present."""
        self.assertFalse(self.config.api_key)
        self.assertFalse(self.config.api_key_prefix)


    def test_none_deletes_user_name_and_password(self):
        """After having used basic authentication, credentials can be deleted."""
        auth.basic("username", "password")
        auth.none()
        self.test_no_authentication_has_no_user_name_and_password()

    def test_basic_authentication_provides_username_and_password(self):
        for username, password in [("a", "p"), ("1", "2")]:
            auth.basic(username, password)
            self.assertIsBasic(username, password)

    def assertIsBasic(self, username, password):
        """Make sure we have basic authentication."""
        self.assertEqual(self.config.username, username)
        self.assertEqual(self.config.password, password)

    def test_api_key(self):
        """Test that the api key creates the correct values."""
        for key in ["api-key", "test", "jfsdgfghdsafdskhgfkadsgkgfkasd"]:
            auth.api_key(key)
            self.assertIsApiKey(key)

    def assertIsApiKey(self, key):
        """Make sure we have api key authentication."""
        settings = self.config.auth_settings()["api_key"]
        self.assertEqual(settings["type"], "api_key")
        self.assertEqual(settings["in"],"header")
        self.assertEqual(settings["key"],"Authorization")
        self.assertEqual(settings["value"],"api-key key=" + base64.b64encode(key.encode()).decode())

    def test_none_deletes_api_key(self):
        """Test deletion of api key."""
        auth.api_key("key")
        auth.none()
        self.test_no_authentication_has_no_api_key()

    def test_basic_removes_api_key(self):
        """The basic auth replaces the api key.

        Else, we might run into troubles with what is used last.
        """
        auth.api_key("key")
        auth.basic("user", "pass")
        self.test_no_authentication_has_no_api_key()

    def test_api_key_removes_basic(self):
        """The api key auth replaces the basic auth.

        Else, we might run into troubles with what is used last.
        """
        auth.basic("user", "pass")
        auth.api_key("key")
        self.test_no_authentication_has_no_user_name_and_password()


if __name__ == '__main__':
    unittest.main()
