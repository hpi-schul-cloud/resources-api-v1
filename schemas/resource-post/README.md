Resource Post
=============

When adding a resource to the Resource API, this is the schema of the posted data.
You can also find this schema described in the [Swagger file #ResourcePost][swagger].
This is the standart and swagger needs to be synced accordinf to this.

Example:
```
{
  "data": {
    "type": "resource",
    "id" : "optional-id",
    "attributes" : {
      "title" : "... see ../resource"
    }
  }
}
```

[swagger]: ../../api-definition/swagger.yml
