#!/bin/bash

cd "`dirname \"$0\"`"

echo "Pass --user as first argument, if the package installatoin failes."

user="$1"
output="python_client"
version_ending="0"
config="python_client_config.json"
if [ -n "$TRAVIS_BUILD_NUMBER" ]; then
  # see https://docs.travis-ci.com/user/environment-variables/
  version_ending="${TRAVIS_BUILD_NUMBER}"
fi


# config values from
#   java -jar generators/swagger-codegen-cli-2.2.2.jar config-help -l python
echo "{
        \"packageName\": \"schul_cloud_resources_api_v1\",
        \"packageVersion\" : \"1.0.0$version_ending\",
        \"packageUrl\" : \"https://github.com/schul-cloud/resources-api-v1\"
      }" > "$config"
echo "Configutation:"
cat "$config"
echo
./generate_code.sh python "$output" --config "$config"

src="../schemas"
dst="./python_client/schul_cloud_resources_api_v1/schema/json"
echo "copying all json files from $src to $dst"
for file in `( cd "$src" && find . -name \*.json )`; do
  mkdir -p "$dst/`dirname \"$file\"`"
  cp -vT "$src/$file" "$dst/$file"
done

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
