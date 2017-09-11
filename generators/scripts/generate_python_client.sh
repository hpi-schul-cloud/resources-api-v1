#!/bin/bash

cd "`dirname \"$0\"`"

echo "Pass --user as first argument, if the package installatoin failes."

user="$1"
output="../python_client"
config="../python_client_config.json"
version="`./version`"

# config values from
#   java -jar generators/swagger-codegen-cli-2.2.2.jar config-help -l python
echo "{
        \"packageName\": \"schul_cloud_resources_api_v1\",
        \"packageVersion\" : \"$version\",
        \"packageUrl\" : \"https://github.com/schul-cloud/resources-api-v1\"
      }" > "$config"
echo "Configuration:"
cat "$config"
echo
./generate_code.sh python "$output" --config "$config"

./copy_schemas_to "../python_client/schul_cloud_resources_api_v1/schema/json"

(
  set -e
  cd "$output"
  echo "jsonschema==2.6.0" >> "requirements.txt"
  python3 -m pip install $user -r requirements.txt \
                               -r test-requirements.txt \
                               wheel tox
  tox
  python3 setup.py sdist bdist_wheel
)
