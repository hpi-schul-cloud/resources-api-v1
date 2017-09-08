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
    if (api.resource.isValid(resource)) {
      console.log("The resource is valid.")
    } else {
      api.resource.validate(resource) // create an error message
    }

There are valid and invalidexamples which you can use:

    var api = require("@schul-cloud/schul-cloud-resources-api-v1");
    console.log("Valid examples:", api.resource.getValidExamples())
    console.log("Invalid examples:", api.resource.getValidExamples())

If you have a look at the [schemas folder][schemas], you can find all
schemas you can use:

    var api = require("@schul-cloud/schul-cloud-resources-api-v1");
    api.resource
    api.error
    api.license
    api.search_response

## Tests & Development

To run the tests, run the following commands for installation:

    npm install -g mocha
    npm install chai

[schemas]: https://github.com/schul-cloud/resources-api-v1/tree/master/schemas
