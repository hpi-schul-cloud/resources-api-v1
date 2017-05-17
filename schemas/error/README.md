# Error

[Discussion](https://github.com/schul-cloud/resources-api-v1/issues/42)

The error format of all content providers should be standardized.
The jsonapi standard defines the error format.
This format extends the [error format][api] specified by the jsonapi.

## Behavior

The usual error response is a json object.
The header `Content-Type: application/vnd.api+json` must be set.

Exception:
If an error occurs which is not expected (500), it is recommended that a jsonapi error
is sent back.
If this can not be done, it is better to send something like the usual error handler.
E.g. if there is an error in your error handler, fall back to the framework.

## Examples

- see the [examples folder](examples)
- see the [jsonapi examples][api-ex]


## Structure

The usual error response is a json object as specified in [the jsonapi specification][api].

Attibutes of the **first** error:

- **jsonapi** (required)  
  As defined in the [search response][sr].
- **errors** (required)  
  A list of errors.
  It must be at least one error present.
  The frist error MUST have the following attributes:
  - **status**  
    The status code, e.g. "400" as a string
  - **title**  
    The title of the status code, see the [list](http://httpstatuses.com/).
  - **detail**  
    A description of why this error occurred.
    In case of a validation error, include the problematic attribute.
    Include source code, ... .

## Related Work
See [stackoverflow](http://stackoverflow.com/a/25637397/1320237) for the jsonschema inplementation hints.

[sr]: ../search-response/README.md
[api]: http://jsonapi.org/format/#errors
[api-ex]: http://jsonapi.org/examples/#error-objects
