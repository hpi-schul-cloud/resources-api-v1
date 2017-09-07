#!/bin/bash
#
# Followed this tutorial to generate the package:
#    https://www.hacksparrow.com/how-to-write-node-js-modules.html
#

set -e

cd "`dirname \"$0\"`"

config="./schul-cloud-resources-api-v1/package.json"
version_ending="0"
if [ -n "$TRAVIS_BUILD_NUMBER" ]; then
  # see https://docs.travis-ci.com/user/environment-variables/
  version_ending="${TRAVIS_BUILD_NUMBER}"
fi
version="1.0.$version_ending"

# see
#    https://docs.npmjs.com/files/package.json
echo "{
        \"name\": \"@schul-cloud/schul-cloud-resources-api-v1\",
        \"version\" : \"$version\",
        \"homepage\" : \"https://github.com/schul-cloud/resources-api-v1\",
        \"description\" : \"The learning resources' api definitions for Schul-Cloud.\",
        \"license\" : \"AGPL-1.0\",
        \"private\" : false,
        \"publishConfig\" : { \"access\" : \"public\" }
      }" > "$config"

(
  cd schul-cloud-resources-api-v1
  npm publish
)