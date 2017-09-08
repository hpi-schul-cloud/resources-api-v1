const path = require("path");
const fs = require("fs");

exports = module.exports = {};

var schemas_path = path.join(__dirname, "schemas");

function Schema(name, path) {

}

fs.readdir(schemas_path, function(err, items) {
  for (var i = 0; i < items.length; i += 1) {
    var item = items[i];
    var name = item.replace("-", "_");
    var schema_path = path.join(schemas_path, item);
    exports[name] = Schema(name, schema_path);
  }
})

