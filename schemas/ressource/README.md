# Ressource

The object specification is based on talks with
- Arne Oberlander
- Nicco Kunzmann
- the Bachelor Project team
- the [content crawler][content-crawl-api]
- Thomas Haubner from tutory, thanks for the input

## Schema

The schema is defined in the [ressource.json](ressource.json) file.
The schema is generated from [the specification][spec].

## Specification
[spec]: #specification

This Ressource Specification is the binding discussion place.
All code and schemas are derived from this document.

A ressource is a JSON object with the following attributes:

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
- **providerLevel** (??)  
  The source can be classified like this:
  - `schul-cloud` - totally trusted information
  - `community` - we know who created this information
  - `external` - someone on the web gave us this information (no authentication)
  The idea:
  - The search always displays schul-cloud and community ressources
  - external ressources are not displayed to kids, teachers can choose
  **TODO**: discuss
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

Content Categories are discussed in [this blog post][cc-blog].
The Content Category is related to the [curriculum][curriculum].





[rdd]: http://tom.preston-werner.com/2010/08/23/readme-driven-development.html
[arch]: https://schul-cloud.github.io/blog/2017-04-24/extensible-content-delivery#architecture
[content-crawl-api]: https://github.com/schul-cloud/schulcloud-content-crawler#attributes
[rfc2046]: https://tools.ietf.org/html/rfc2046
[ieee-lom]: http://129.115.100.158/txlor/docs/IEEE_LOM_1484_12_1_v1_Final_Draft.pdf
[swag-1]: https://app.swaggerhub.com/apis/niccokunzmann/schul-cloud-content-api/1.0.0
[schemas]: ./schemas
[api-definition]: ./api-definition/
[pypi]: https://pypi.python.org/pypi/schul-cloud-ressources-api-v1
[travis]: https://travis-ci.org/schul-cloud/ressources-api-v1
[api-definition]: api-definition
[ressource-schema]: schema/resource
[schemas]: schemas
[generators]: generators
[scripts]: scripts
[python-library]: generators/python_client/
[cc-blog]: https://schul-cloud.github.io/blog/2017-04-26/api-ressources-specification#content-categories
[curriculum]: ../curriculum#readme