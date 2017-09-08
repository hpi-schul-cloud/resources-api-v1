#!/bin/bash
#
# Followed this tutorial to generate the package:
#    https://www.hacksparrow.com/how-to-write-node-js-modules.html
#

set -e

cd "`dirname \"$0\"`"

output="./schul-cloud-resources-api-v1"
config="$output/package.json"
version="`../scripts/version`"
schemas="$output/schemas"

echo "# Copy schemas to package"

../scripts/copy_schemas_to "$schemas"

# see
#    https://docs.npmjs.com/files/package.json
echo "{
        \"name\": \"@schul-cloud/schul-cloud-resources-api-v1\",
        \"version\" : \"$version\",
        \"homepage\" : \"https://github.com/schul-cloud/resources-api-v1\",
        \"description\" : \"The learning resources' api definitions for Schul-Cloud.\",
        \"license\" : \"AGPL-1.0\",
        \"private\" : false,
        \"publishConfig\" : { \"access\" : \"public\" },
        \"files\" : [
`
          for file in \`( cd "$output" && find schemas -name \*.json )\`; do
            echo "          \\\"$file\\\","
          done
        `
          \"LICENSE\",
          \"schul-cloud-resources-api-v1.js\",
          \"README.md\"
        ]
      }" > "$config"

echo "# Config: "
cat "$config"
echo

cp ../../LICENSE "$output" 

# TODO: test the package

(
  cd "$output"
  echo "# Generating package: "
  npm pack
)
