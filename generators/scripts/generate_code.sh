#!/bin/bash
set -e

# parameters
language="$1"
shift
output="$1"
shift

mkdir -p "$output"

cd "`dirname \"$0\"`"

echo "# Downloading code generator"
version="2.2.2"
jar="swagger-codegen-cli-$version.jar"
wget -c "http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/$version/$jar"

echo "Generating code"
# see https://github.com/swagger-api/swagger-codegen#getting-started
java -jar "$jar" generate \
     -i ../../api-definition/swagger.yaml \
     -l "$language" \
     -o "$output" "$@"





