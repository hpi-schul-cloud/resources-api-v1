# schul-cloud-resources-api-v1

This module contains the schemas and examples of the api definitions.

You can install this package by running

    npm install @schul-cloud/schul-cloud-resources-api-v1

## Usage

You can use the module to validate resource attributes:

    var api = require("@schul-cloud/schul-cloud-resources-api-v1");
    var resource = {
      "title": "Test",
      "url": "http://example.org"
    }
    if (api.schemas.resource.isValid(resource)) {
      console.log("The resource is valid.")
    } else {
      api.resource.validate(resource) // create an error message
    }

There are valid and invalidexamples which you can use:

    var api = require("@schul-cloud/schul-cloud-resources-api-v1");
    console.log("Valid examples:", api.schemas.resource.getValidExamples())
    console.log("Invalid examples:", api.schemas.resource.getValidExamples())

If you have a look at the [schemas folder][schemas], you can find all
schemas you can use:

    var api = require("@schul-cloud/schul-cloud-resources-api-v1");
    api.schemas.resource
    api.schemas.error
    api.schemas.license
    api.schemas.search_response
    
You can list all of them with

    api.getSchemaNames()

Each `schema` in the `api.schemas` has certain attributes and functions:

- `schema.name`
   is the name of the schema.
- `schema.getValidExamples()`
  return a list of valid examples for the schema.
- `schema.getInvalidExamples()`
  return a list of invalid examples for the schema.
- `schema.isValid(object)`
  validates the object against the schema and returns true if the
  schema is valid for this object.
- `schema.getValidationErrors(object)`
  return a list of `ValidationErrors` which explain the problems in the
  object if it should be valid for the schema.
- `schema.getSchema()`
  return the raw jsonschema.
- `schema.getId()`
  return the identifier of the raw schema.

## Tests & Development

To run the tests, run the following commands for installation:

    npm install -g mocha
    npm install chai


---

You can [edit this file on GitHub][this].

[schemas]: https://github.com/schul-cloud/resources-api-v1/tree/master/schemas
[this]: https://github.com/schul-cloud/resources-api-v1/tree/master/generators/node/schul-cloud-resources-api-v1/README.md
