# coding: utf-8

"""
    Schul-Cloud Content API

"""


from __future__ import absolute_import

import os
import sys
import unittest

import schul_cloud_ressources_api_v1
from schul_cloud_ressources_api_v1.schema import (
    validate_ressource, is_valid_ressource, get_valid_examples, get_invalid_examples
)


class TestSchema(unittest.TestCase):
    """ Schema unit test stubs """

    def test_there_are_valid_examples(self):
        assert get_valid_examples()

    def test_there_are_invalid_examples(self):
        assert get_valid_examples()


if __name__ == '__main__':
    unittest.main()
