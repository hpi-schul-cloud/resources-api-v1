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
schemas="$output/lib/schemas"

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
        \"repository\": {
          \"type\" : \"git\",
          \"url\" : \"https://github.com/schul-cloud/resources-api-v1.git\"
        },
        \"private\" : false,
        \"publishConfig\" : { \"access\" : \"public\" },
        \"files\" : [
`
          for file in \`( cd "$output" && find lib/schemas -name \*.json )\`; do
            echo "          \\\"$file\\\","
          done
        `
          \"LICENSE\",
          \"README.md\",
          \"lib/index.js\",
          \"lib/validator.js\",
          \"test/test.js\"
        ],
        \"directories\" : {
          \"test\": \"test\",
          \"lib\" : \"lib\"
        },
        \"main\" : \"lib/index.js\",
        \"dependencies\": {
          \"ajv\" : \"5.2.2\",
            \"co\" : \"4.6.0\",
            \"fast-deep-equal\" : \"1.0.0\",
            \"json-schema-traverse\" : \"0.3.1\",
            \"json-stable-stringify\" : \"1.0.1\",
              \"jsonify\" : \"0.0.0\"
        },
        \"devDependencies\" : {
          \"chai\" : \"4.1.2\",
          \"mocha\" : \"3.5.0\"
        },
        \"scripts\" : {
          \"test\": \"npm run mocha\",
          \"mocha\": \"mocha test/ --recursive\"
        }
      }" > "$config"

echo "# Config: "
cat "$config"
echo

cp ../../LICENSE "$output" 

# TODO: test the package

(
  set -e
  cd "$output"
  echo "# Generating package:"
  npm pack
  echo "# Install dependecies:"
  npm install
  echo "# Run tests"
  npm test
)
