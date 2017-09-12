const path = require("path");
const fs = require("fs");

exports = module.exports = {};

var schemas_path = path.join(__dirname, "schemas");
var validator = require("./validator");


function getJSONFilesFromDirectory(directory) {
  var files = [];
  fs.readdirSync(directory).forEach(function(item){
    if (item.toLowerCase().endsWith(".json")) {
      var item_path = path.join(directory, item);
      var required = require(item_path);
      files.push(required);
    }
  });
  return files;
}

function Schema(filename, schema_path) {
  this.filename = filename + ".json";
  this.name = filename.replace("-", "_");
  this.path = schema_path;
  this._schema = require(path.join(this.path, this.filename));
  this.getValidExamples = function() {
    return getJSONFilesFromDirectory(path.join(this.path, "examples", "valid"));
  }
  this.getInvalidExamples = function() {
    return getJSONFilesFromDirectory(path.join(this.path, "examples", "invalid"));
  }
  this.isValid = function(object) {
    return validator.validate(this.getId(), object);
  }
  this.getValidationErrors = function(object) {
    return this.isValid(object).errors;
  }
  this.getSchema = function() {
    return this._schema;
  }
  this.getId = function() {
    return this.getSchema().id;
  }
}

var schemaNames = [];

exports.getSchemaNames = function(){
  return schemaNames;
}
exports.schemas = {};
exports.ajv = validator;

fs.readdirSync(schemas_path).forEach(function(item) {
  var schema_path = path.join(schemas_path, item);
  var schema = new Schema(item, schema_path);
  exports.schemas[schema.name] = schema;
  schemaNames.push(schema.name);
  validator.addSchema(schema.getSchema());
})

