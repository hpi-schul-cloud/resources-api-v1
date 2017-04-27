# ressources-api-v1

The API specification to add content to the Schul-Cloud.
This is the [Ressources-=API form the architecture][arch]

If you like to work on this on bring in new ideas, you can open an issue and discuss with us.

## Structure

To verify your requests and responses, the is specified as follows:
- This README contains a complete description of
  - Objects 
    - with all attributes
    - their description
    - examples
    - points unclear that need to be specified, marked with a **TODO**
    - their dependencies on other attributes
  - endpoints
    - described like objects
- The `schema` folder contains the JSON-Schema to verify the different formats
- The `docker` folder contains a test-endpoint which can be used to test you application against.

## Endpoints

- TODO


  klassenstufe
  thumbnail
  size
  dimensions
  duration
  carl
  contextUrl - wikimedia: image+license+verisons, ...
  
### Search

- **/v1/search?q=WORDS?ATTRBUTE=...&ATTRBIUTE2=...?$skip=SKIP?$limit=LIMIT**  
  Inspiration: [feathers](https://docs.feathersjs.com/api/databases/querying.html)
  - **q** (required)  
    The query string `WORDS`. They should search at least these object attributes:
    - title
    - content
  - **ATTRIBUTE** (optional)  
    To filter attributes of the objects.
    Example: `title=my%20title`  
    All objects returned must have the filter applied.
    Filtering must work with strings. It can work with other types.
    If an attribute is filtered which is an array, the value must be inside the array.
    Example:
    ```
    objects: [ {"license": ["MIT", "GPL"]}, {"license": ["MIT"]} ]
    query: "?license=GPL"
    result:  [ {"license": ["MIT", "GPL"]} ]
    ```
  - pagination inspired by [feathers](https://docs.feathersjs.com/api/databases/common.html#pagination).
    - `$skip` (optional)   
      a positive integer  
      how many object shall be skipped.
      If more objects are skipped than are there, data is empty.
    - `$limit` (optional)
      how many object shall be returned.  
      This is the maximum number of objects that shall be returned.
      Less objects can be returned.
  Result:
  ```
  {
    "total": "<total number of records>",
    "limit": "<max number of items per page>",
    "skip": "<number of skipped items (offset)>",
    "data": [/* data */]
  }
  ```
  - `data` is a list of ressource objects sorted by relevance
  - Headers:
    - `link` as defined in [RFC5988](https://tools.ietf.org/html/rfc5988)  
      Relations: 
      - `previous` defined by all but the first page
      - `next` defined by all but the last page
      Example: `Link: </TheBook/chapter2>; rel="previous", </TheBook/chapter4>; rel="next"`
    

## Research

DONE

- **LOM**  
  LOM shall be an inspiration. [Wikipedia](https://en.wikipedia.org/wiki/Learning_object_metadata)
- **Schema.org**  
  http://schema.org/docs/gs.html  
  These schemata are used on web-sites to mark parts the of HTML site as specific content.
  This is useful if the search engine outputs HTML.
  E.g. an author can be shown in the [Person](http://0.3-2e.schemaorgae.appspot.com/Person) schema.
  - schema.org: http://0.3-2e.schemaorgae.appspot.com/CreativeWork
    -> provider
- **Learning Object**  
  https://en.wikipedia.org/wiki/Learning_object
  - [IEEE LOM](129.115.100.158/txlor/docs/IEEE_LOM_1484_12_1_v1_Final_Draft.pdf)
    for 
    - Learning object interactivity
    - 7. LangString
      - `DateTime`
      - `Language` 
    - 5.2 `Learning Resource Type`
    - 5.1 `Interactivity Type` active, expositive, mixed
    - 5.9 Typical learning time
    - 5.8 difficulty
    - 5.7 typical age range

TODO

- bildungsserver, apache lucene, elixier - statt elastisearch

- Example: http://dsb-client.readthedocs.io/en/latest/descriptions.html

## Further Reading
- [README Driven Development][rdd]

[rdd]: http://tom.preston-werner.com/2010/08/23/readme-driven-development.html
[arch]: https://schul-cloud.github.io/blog/2017-04-24/extensible-content-delivery#architecture