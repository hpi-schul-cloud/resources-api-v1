# Search Reponse

The search response object for the search engines.
All search engines should create output in this format.

In this folder you can find

- [the description][description]
- valid and invalid [examples](examples)
- [the schema][schema] to validate responses

## Description
[description]: #description

The response must be compatible to the [JSONAPI specification 1.0][jsonapi].

There are error responses and successful responses.
A successful response is

- [**200**](http://jsonapi.org/format/#fetching-resources-responses-200)  
  This is a response to a successful query of resources.
  The result is a [Search Response][search-response]
- [**400**](http://jsonapi.org/format/#fetching-sorting)  
  Equivalent to the sorting, if the server does not support the required parameters,
  it must return `400 Bad Request`.

  > If the server does not support sorting as specified in the query parameter sort, it MUST return 400 Bad Request
  
  Equivalent to the error responses of the [resources api][resource-api],
  this must be a JSONAPI-compatible response with some more information.
- **404**  
  The server must not return a 404 response if no resources were found.
  The server instead returns a `200 OK` with an empty `data` array.
  404 is reseved for invalid paths.

## Search Reponse
[search-response]: #search-response

For the example responses, please see the [examples/valid](examples/valid) folder.

Fields:

- **jsonapi** (required)  
  Informtation about the server.
  ```
  {
    "version": "1.0",
    "meta" : {
      "name": "Example Server",
      "source": "https://github.com/schul-cloud/resources-api-v1",
      "description": "This is just an eampel server for the search API."
    }
  }
  ```
- **links** (required)  
  This are the links for the pagination [as defined in the jsonapi](http://jsonapi.org/format/#fetching-pagination).
  Example for querying <http://url.used.to/get/this/document> and getting 5 resources back:
  ```
  {
    "self": {
      "href": "http://url.used.to/get/this/document?page[offset]=15&page[limit]=5",
      "meta": {
        "count": 5,
        "offset": 15,
        "limit": 5
      }
    },
    "first": "http://url.used.to/get/this/document?page[offset]=0&page[limit]=5",
    "last": "http://url.used.to/get/this/document?page[offset]=50&page[limit]=5",
    "prev": "http://url.used.to/get/this/document?page[offset]=10&page[limit]=5",
    "next": "http://url.used.to/get/this/document?page[offset]=20&page[limit]=5"
  }
  ```
  `first`, `last`, `prev` and `next` must be `null` if they are not available.
  If they exist, they MUST be set to valid values.
  It is recommended to use the HTTP `Host` header field to set the absolute url.
  The urls must be absolute urls.
  
  - `count` is the actual number of object retrieved.
  - `offset` is the start index in the list of objects.
  - `limit` is the requested number of objects.
  
  Edge cases:
  
  - If the end of the resource list is reached, `count` may be less than limit.
  - If the `limit` is higher than the maximum limit the server has internally, the server sets the `limit` to the maximum available limit.
  - If there are no resources, `first`, `last`, `prev` and `next` MUST be `null`.
  - If there is no end in sight, `last` MUST be `null`
  - If the last page is reached, `next` MUST be `null`.
  - If `last` is given, `next` must be given.
  - If `first` is given, `prev` must be given.
  - On all pages except the last, the sever SHOULD return as many objects as in `limit`, thus `count` SHOULD be equal to `limit`.
  - The `prev` and `next` links MUST not skip objects.
  - If the end of the resource list is reached, count may be less than limit.  
    This implies that 
    - there is no next link and 
    - if there are resources, the last link is self 
    - if there are no resources in this request
      - the last link is pointing to a lesser offset or
      - the last link is null
  
- **data** (required)  
  This is an array of [JSONAPI resource objects](http://jsonapi.org/format/#document-resource-objects).
  Example:
  ```
  {
    "type": "resource",
    "id": "resource-xy",
    "links": {
      "self": "http://resource.server/resources/resource-xy"
    },
    "attributes": {
      ... a valid learning resource ...
    }
  }
  ```
  - **type** (required)  
    This must be `"resource"`.
  - **id** (required)  
    This is an id identifying the resource at the server.
  - **links** (optional)  
    `self`: A url to retrieve the resource.
    As resources may be in a database, this link comes in handy when retrieving the resource separately.
    If the resource can not be retrieved without authentication, there should be a hint in the `meta` object `"authentication": "required"`.
    When resources are generated on the fly, it might be hard to generate a link for them. This is why this is optional.
  - **attributes** (required)  
    These are the attributes of the object as specified in the [resource schema][res]



[schema]: search-response.json
[jsonapi]: http://jsonapi.org/format/
[resource-api]: ../../README.md#resources-api
[res]: ../resource/
