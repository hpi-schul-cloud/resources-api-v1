#!/bin/bash
#
# Followed this tutorial to generate the package:
#    https://www.hacksparrow.com/how-to-write-node-js-modules.html
#

set -e

cd "`dirname \"$0\"`"

config="./schul-cloud-resources-api-v1/package.json"
version="`../scripts/version`"

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

../scripts/copy_schemas_to "schul-cloud-resources-api-v1/schemas"

(
  cd schul-cloud-resources-api-v1
  npm publish
)
