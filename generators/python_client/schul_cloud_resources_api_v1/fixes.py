"""This module fixes some broken code from the generator.

"""
from schul_cloud_resources_api_v1.models.resource_response_links import ResourceResponseLinks

#
# Fix the _self attribute to be self
#

ResourceResponseLinks.self = ResourceResponseLinks.__dict__["_self"]