#!/bin/bash

cd "`dirname \"$0\"`"

output="python_server"
config="python_server_config.json"

# config values from
#   java -jar generators/swagger-codegen-cli-2.2.2.jar config-help -l python
echo "{
        \"packageName\": \"schul_cloud_ressources_server_tests_v1\",
        \"packageVersion\" : \"1.0.0$version_ending\",
        \"packageUrl\" : \"https://github.com/schul-cloud/ressources_server_tests_v1\"
      }" > "$config"
echo "Configutation:"
cat "$config"
echo
./generate_code.sh python-flask "$output" --config "$config"

(
  cd "$output"
  python3 -m pip install -r requirements.txt \
                         -r test-requirements.txt \
                         wheel
  python3 -m nosetests
)
