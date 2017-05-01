schul_cloud_ressources_api_v1
=============================

The ressources API package allows easy access to the Schul-Cloud ressources servers.
To get an overview about how the api is defined, please refer to the repository_.

Installation
------------

You can install the package with pip from PyPI_

.. code:: shell

    pip install schul_cloud_ressources_api_v1

Accessing the API
-----------------

Suppose, a server runs under http://localhost:8080/v1.
You can use the api to connect to it.
If you do not have a server, you can get a test server from the package
`schul_cloud_ressources_server_tests`_.

.. code:: Python

    # import the api classes for access
    from schul_cloud_ressources_api_v1 import ApiClient, RessourceApi

    # create the client objects
    url = "http://localhost:8080/v1"
    client = ApiClient(url)
    api = RessourceApi(client)

The `api` object gives access to the server.
Here, you can see how to access the api:

.. code:: Python

    # import the ressource examples
    from schul_cloud_ressources_api_v1.schema import get_valid_examples

    # get a valid ressource
    ressource = get_valid_examples()[0]
    print(ressource)
    
    # add the ressource to the server
    response = api.add_ressource(ressource)

    # verify the ressource is on the server
    all_my_resssources_on_the_server = api.get_ressource_ids()
    assert response.id in all_my_resssources_on_the_server

    # get the ressource from the server
    ressource_copy = api.get_ressource(response.id)
    assert ressource_copy == ressource

    # delete the ressource
    api.delete_ressource(response.id)

Verifying Ressources
~~~~~~~~~~~~~~~~~~~~

When you use ressources, you may want to verify if they have the correct format.
The format is specified in the `ressource-schema <https://github.com/schul-cloud/ressources-api-v1/tree/master/schemas/ressource>`_.
This schema is included in the api.

.. code:: Python

    from schul_cloud_ressources_api_v1.schema import (
        get_valid_examples, get_invalid_examples, validate_ressource, is_valid_ressource
    )

You can test if a ressource is valid or not using `is_valid_ressource`

.. code:: Python

    valid_ressource = get_valid_examples()[0]
    assert is_valid_ressource(valid_ressource)

    invalid_ressource = get_invalid_examples()[0]
    assert not is_valid_ressource(invalid_ressource)

If you would like to find outmore about why the ressource is not valid, you can use `validate_ressource`.

.. code:: Python

    validate_ressource({'title': 'hello'})

Which results in an error that the `url` property is not present but is required.

.. code:: Python

    jsonschema.exceptions.ValidationError: 'url' is a required property
    
    Failed validating 'required' in schema:
        {'properties': {'contentCategory': {'$ref': '#/definitions/ContentCategory'},
                        'contextUrl': {'$ref': '#/definitions/URL'},
                        'curricula': {'items': {'$ref': '../curriculum/curriculum.json'},
                                      'type': 'array'},
                        'dimensions': {'$ref': '#/definitions/Dimensions'},
                        'duration': {'type': 'number'},
                        'languages': {'description': 'As described in IEEE '
                                                     'LOM, Section 1.3 '
                                                     'http://129.115.100.158/txlor/docs/IEEE_LOM_1484_12_1_v1_Final_Draft.pdf',
                                      'items': {'$ref': '#/definitions/Language'},
                                      'type': 'array'},
                        'licenses': {'items': {'$ref': '../license/license.json'},
                                     'type': 'array'},
                        'mimeType': {'description': 'https://tools.ietf.org/html/rfc2046',
                                     'example': 'text/html',
                                     'type': 'string'},
                        'size': {'format': 'int64', 'type': 'integer'},
                        'thumbnail': {'$ref': '#/definitions/URL'},
                        'title': {'description': 'The title of the ressource.',
                                  'example': 'Schul-Cloud',
                                  'type': 'string'},
                        'url': {'$ref': '#/definitions/URL'}},
         'required': ['title',
                      'url',
                      'licenses',
                      'mimeType',
                      'contentCategory',
                      'languages'],
         'type': 'object'}
    
    On instance:
        {'title': 'hello'}

Related Packages
----------------

The `Server Tests <https://github.com/schul-cloud/schul_cloud_ressources_server_tests>`_ use this library to test servers implementing the API defined in the repository_.

Further Reading
---------------

- To edit this description, you can edit the `file on Github <https://github.com/schul-cloud/ressources-api-v1/tree/master/generators/python_client/README.rst>`__.
  You can use `this editor <http://rst.ninjs.org/>`__.







.. _repository: https://github.com/schul-cloud/ressources-api-v1
.. _PyPI: https://pypi.python.org/pypi/schul-cloud-ressources-api-v1
.. _schul_cloud_ressources_server_tests: https://github.com/schul-cloud/schul_cloud_ressources_server_tests