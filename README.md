# ressources-api-v1

The API specification to add content to the Schul-Cloud.
This is the [Ressources API form the architecture][arch]

If you like to work on this on bring in new ideas, you can open an issue and discuss with us.

## Structure

To verify your requests and responses, the is specified as follows:
- This README contains a complete description of
  - [Objects][objects]
    - with all attributes
    - their description
    - examples
    - points unclear that need to be specified, marked with a **TODO**
    - their dependencies on other attributes
  - [endpoints][endpoints]
    - described like objects
- The `schema` folder contains the JSON-Schema to verify the different formats
- The `docker` folder contains a test-endpoint which can be used to test you application against.

## Objects
[objects]: #objects

The object specification is based on talks with
- Arne Oberlander
- Nicco Kunzmann
- the Bachelor Project team
- the [content crawler][content-crawl-api]
- TODO: Thomas Haubner from tutory

Attributes:

- **title** (required)  
  The title of the document.
- **url** (required)  
  The location of the content.  
  It should be HTTP/HTTPS.
- **license** (required)  
  An array of specified lincese strings.
  **TODO**: Ask tutory about their model for remix.
- **provider** (required)  
  The entity providing this information, e.g. "Westermann" or "Schul-Cloud user xyz"
  **TODO**: Ask tutory about their model for remix. Maybe this flows into the license.
- **mimeType** (required)  
  The mime type as defined in [RFC2046][rfc2046]
- **contentCategory** (required)  
  As defined [here][content-category].
  Values:
  - `"a"` for atomic
  - `"l"` for learning object
  - `"rl"` for lerning object conform to at least one Rahmenlehrplan
  - `"t"` tool
- **subjects** (...)  
  - required if `contentCategory` is `"rl"`
  - else optional
  **TODO**: specify an extensible list (recommendation) for subject strings
- **languages** (required)  
  A list of languages given by country code.
  This is specified in [IEEE-LOM, Section 1.3][ieee-lom]
  Examples: `de`, `de-ch`
- **class** (optional)  
  An array specifying the recommended school class.
  Examples: `[7]`, `[8, 9]`
  **TODO**: verify that this is important.
- **thumbnail** (optional)  
  A url to the preview image.
  This could be the first page of a PDF, a small version of an SVG or PNG image.
- **size** (optional)  
  The size in bytes to download the source.  
  This is recommended for pictures, PDFs, ...
  Interactive content may vary in size, so this is not a must.  
  Reference: [IEEE LOM, 4.2][ieee-lom]
- **dimensions** (optional)  
  In case of pictures and movies, this is the resolution e.g. `640pxX480px`.
  In case of a PDF, this could also be "A4" or "letter", ...
  **TODO**: speicify the dimensions.
- **duration** (optional)  
  Form movies and clips, things that take time, this is the duration it takes
  to go though the object in default time.
  The unit is seconds. The type is float.  
  Reference: [IEEE LOM, 4.7][ieee-lom]
- **contextUrl** (optional)  
  This is the url with moer context about the `url`.
  The contenxt provides more information about the object like license, versions, ...
  The url best referes to a page using [schema](http://schema.org/).
  Example:
  - url is https://upload.wikimedia.org/wikipedia/commons/8/8a/LOM_base_schema.svg  
    contextUrl is https://en.wikipedia.org/wiki/File:LOM_base_schema.svg


### Content Category
[content-category]: #content-category


## Endpoints
[endpoints]: #endpoints

These are the API endpoints defined in the [documentation][arch].

### Ressources

[Current Swagger implementation][swag1]

- `GET /v1/ressources?$skip=SKIP?$limit=LIMIT`  
  Returns a paginated list of ressources, see [the search result][search].
- `POST /v1/ressources`  
  Add a ressource.
  Get the ressource back as the server sees it.
  





### Search
[search]: #search

- `GET /v1/search?q=WORDS?ATTRBUTE=...&ATTRBIUTE2=...&$skip=SKIP?$limit=LIMIT`  
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
    If an attribute is filtered but not present, the object is not chosen.
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
    - `Link` as defined in [RFC5988](https://tools.ietf.org/html/rfc5988)  
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
  - [IEEE LOM][ieee-lom]
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
- [HTTP statuses](https://httpstatuses.com/)

[rdd]: http://tom.preston-werner.com/2010/08/23/readme-driven-development.html
[arch]: https://schul-cloud.github.io/blog/2017-04-24/extensible-content-delivery#architecture
[content-crawl-api]: https://github.com/schul-cloud/schulcloud-content-crawler#attributes
[rfc2046]: https://tools.ietf.org/html/rfc2046
[ieee-lom]: http://129.115.100.158/txlor/docs/IEEE_LOM_1484_12_1_v1_Final_Draft.pdf
[swag-1]: https://app.swaggerhub.com/apis/niccokunzmann/schul-cloud-content-api/1.0.0
