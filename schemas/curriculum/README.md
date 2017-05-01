# Curriculum

This is the specification of the curricula to use.
Here, we list all the curricula available and the corresponding identifiers.
This list determines the [schema][schema].

## String Format

`<CONFERENCE> :: <BUNDESLAND> :: <SUBJECT> :: <VERSION>`

- `<CONFERENCE>` should be replaced by the entity that standardizes.
- `<BUNDESLAND>` is the area the curriculum is for.
- `<SUBJECT>` is the e.g. `Deutsch` - the subject the curriculum specifies.
- `<VERSION>` is the date or version of the curriculum.

## Curriculum list

If you add something here, also put it into the [schema][schema].

- `KMK :: Thürungen :: Deutsch :: 1978` [PDF](http://link.zu/arnes/fund/oder/anderen/seiten/zum/abrufen)  
  This is an example. In 1978 the KMK came together and standardized the curriculum for the Subject Deutsch in Thuringia.

## JSON Schema

The [schema][schema] is used in the machine specification, in our data bases and searches.
If a content can be categorized as "rl" (`contentCategory`, [source][api]), it must have a
`curriculum` list.
The elements form above can be elements of the curriculum list.

[schema]: curriculum.json
[api]: https://github.com/schul-cloud/ressources-api-v1#objects
