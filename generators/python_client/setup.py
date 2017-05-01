# coding: utf-8

"""
    Schul-Cloud Content API

    This is the specification for the content of Schul-Cloud. You can find more information in the repository <https://github.com/schul-cloud/ressources-api-v1>. 

    OpenAPI spec version: 1.0.0
"""


import sys
import os
from setuptools import setup, find_packages

NAME = "schul_cloud_ressources_api_v1"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

HERE = os.path.dirname(__file__) or "."

REQUIRES = [line.strip() for line in open(os.path.join(HERE, "requirements.txt").readlines()) if line.strip()]

setup(
    name=NAME,
    version=VERSION,
    description="Schul-Cloud Content API",
    author_email="",
    url="https://github.com/schul-cloud/ressources-api-v1",
    keywords=["Swagger", "Schul-Cloud Content API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is the specification for the content of Schul-Cloud. You can find more information in the repository &lt;https://github.com/schul-cloud/ressources-api-v1&gt;. 
    """
)
