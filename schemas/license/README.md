# License

This is a schema for licenses.
As outlined in [this answer][sof1],
we can define different schemas for different licenses and a license
matches them all.

## Schema

Each type of license can have its own schema.
If you find a license schema which is close to yours, consider using this
instead of defning a new one.

## Wikimedia Schema

- **value** (required)  
  This is the name of the license.
  You can find more [on wikimedia][licenses-wikimedia].
- **copyrighted** (required)  
  Whether the license has conditions on copying such as naming the author.
  The value specifies this.

## Further Reading

- [DMCI Metadata Terms][dcmi]
- [#5 Discussion about licenses](https://github.com/schul-cloud/resources-api-v1/issues/5)

[sof1]: http://stackoverflow.com/questions/18375506/how-to-use-dependencies-in-json-schema-draft-04/18384131#18384131
[dcmi]: http://dublincore.org/documents/2012/06/14/dcmi-terms/?v=terms
[licenses-wikimedia]: https://commons.wikimedia.org/wiki/Commons:Lizenzvorlagen#Freie_.E2.80.9ECreative-Commons-Lizenzen.E2.80.9C
