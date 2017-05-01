# Generators

These files generate the source code you can use as a base for your
clients and servers.

Generation uses the [swagger-codegen][swagger-codegen] repository.
We generate

- Python server
- Python Client
  - with upload to pypi
- upload all generated code to the github releases


## Installation

Install Java:

    sudo apt-get -y install default-jre python3-pip

## Usage

You can generate the [python client](https://pypi.python.org/pypi/schul-cloud-ressources-api-v1) like this:

    ./generate_python_client.sh
    
You can generate the server like this:

    ./generate_python_server.sh
    
Additionally, you may want to have a look at [the server tests](https://github.com/schul-cloud/schul_cloud_ressources_server_tests) if you want to implement a server.

[swagger-codegen]: https://github.com/swagger-api/swagger-codegen 
