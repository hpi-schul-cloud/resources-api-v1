# Resource

The object specification is based on talks with
- Arne Oberlander
- Nicco Kunzmann
- the Bachelor Project team
- the [content crawler][content-crawl-api]
- Thomas Haubner from tutory, thanks for the input

## Schema

The schema is defined in the [resource.json][schema] file.
The schema is generated from [the specification][spec].

## Specification
[spec]: #specification

This Resource Specification is the binding discussion place.
All code and schemas are derived from this document.

A resource is a JSON object with the following attributes:

- **title** (required)  
  The title of the document.
- **url** (required)  
  The location of the content.  
  It should be HTTP/HTTPS.
- **licenses** (required)  
  An array of specified lincese strings.
  **TODO**: Ask tutory about their model for remix. [#5](https://github.com/schul-cloud/resources-api-v1/issues/5)
- **mimeType** (required)  
  The mime type as defined in [RFC2046][rfc2046]
- **contentCategory** (required)  
  As defined [here][content-category].
  Values:
  - `"a"` for atomic
  - `"l"` for learning object
  - `"rl"` for lerning object conform to at least one Rahmenlehrplan
  - `"t"` tool
- **languages** (required)  
  A list of languages given by country code.
  This is specified in [IEEE-LOM, Section 1.3][ieee-lom]
  Examples: `de`, `de-ch`
- **thumbnail** (optional)  
  A url to the preview image.
  This could be the first page of a PDF, a small version of an SVG or PNG image.
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
  This is the url with more context about the `url`.
  The contenxt provides more information about the object like license, versions, ...
  The url best referes to a page using [schema](http://schema.org/).
  Example:
  - url is https://upload.wikimedia.org/wikipedia/commons/8/8a/LOM_base_schema.svg  
    contextUrl is https://en.wikipedia.org/wiki/File:LOM_base_schema.svg
- **providerName** (optional)  
  This is the provider of the resource. Examples are be "Wikipedia" or "Khan Academy" or
  a special channel on YouTube like "The Simple Club".

If you like to have a new attribute, change one, delete it or change this document, please see the how to section below.

### Content Category
[content-category]: #content-category

Content Categories are discussed in [this blog post][cc-blog].
The Content Category is related to the [curriculum][curriculum].

## How To Specify

If you like to tell others about your implementation of resource attributes, this specification document might be the right place.
The goal is for each attribute to be the form to describe the use-case. E.g. we do not want to have two title attributes.

### How to Add a New Attribute

You created a new attribute which is useful for your search engine or crawler?
Then, you can follow this process to add the attribute:

1. Create [a new issue][new-issue] describing your attibute. Cover the following:
   - Is there an implementation?
   - What is the purpose?
   - What does it look like?
   - Is it optional or required?
  
   This allows other people to comment and think about if they need something like it.

2. Create a pull-request with your changes. If you do not know how to do that, you can get help.
   1. change [this file][this] to include a description of the form
      ```
      - **attribute name** (optional|required)  
        A description of what it is for and examples
      ```
   2. change the [json schema][schema] file to include your attribute.
      This makes it testable for others if they use your attribute properly.
      Also it prevents others from using it in a wrong way, not having read the updated specification.
   3. Add valid and invalid [exampes][examples] of resources using your atttribute.
   
   Once the pull-request is created, you can modify it and get feedback.
   It should be merged within a week.

### How to Delete an Attribute

If an attribute is not used any more, you can delete it.

1. create an [issue][new-issue] to delete the attribute.
2. Create a pull-request for this attribute with these parts deleted:
   - the attribute descrition in [this file][this].
   - the [json schema description][schema] of the attribute
   - the occurrences of the [examples][examples] using you attribute
   
## How to Change an Attribute

In general, [please open an issue][new-issue] to change the specification for the way you want it to have.
If it is just a misspelling or a minor change, you do not need to do that and can create a pull-request immidietly.

[rdd]: http://tom.preston-werner.com/2010/08/23/readme-driven-development.html
[arch]: https://schul-cloud.github.io/blog/2017-04-24/extensible-content-delivery#architecture
[content-crawl-api]: https://github.com/schul-cloud/schulcloud-content-crawler#attributes
[rfc2046]: https://tools.ietf.org/html/rfc2046
[ieee-lom]: http://129.115.100.158/txlor/docs/IEEE_LOM_1484_12_1_v1_Final_Draft.pdf
[swag-1]: https://app.swaggerhub.com/apis/niccokunzmann/schul-cloud-content-api/1.0.0
[schemas]: ./schemas
[api-definition]: ./api-definition/
[pypi]: https://pypi.python.org/pypi/schul-cloud-resources-api-v1
[travis]: https://travis-ci.org/schul-cloud/resources-api-v1
[api-definition]: api-definition
[resource-schema]: schema/resource
[schemas]: schemas
[generators]: generators
[scripts]: scripts
[python-library]: generators/python_client/
[cc-blog]: https://schul-cloud.github.io/blog/2017-04-26/api-resources-specification#content-categories
[curriculum]: ../curriculum#readme
[new-issue]: https://github.com/schul-cloud/resources-api-v1/issues/new
[this]: README.md
[schema]: resource.json
[examples]: examples
