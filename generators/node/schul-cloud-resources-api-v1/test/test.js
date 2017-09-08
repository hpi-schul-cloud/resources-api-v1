var expect = require("chai").expect;
var api = require("../lib/main.js");
var schemas = api.schemas;

describe("api", function(){
  describe("schemas", function() {
    var names = ["resource", "error", "search_response"];
    names.forEach(function(name) {
      it("must contain a \"" + name + "\" schema", function() {
        expect(schemas).to.have.a.property(name);
      })
      it("must list the \"" + name + "\" schema", function() {
        expect(api.getSchemaNames()).to.include(name)
      })
    })
  })
  api.getSchemaNames().forEach(function(name){
    var schema = schemas[name];
    describe("schema \"" + name + "\"", function(){
      it("must have a name property", function() {
        expect(schema).to.have.a.property("name", name);
      })
      it("must have valid examples", function() {
        var validExamples = schema.getValidExamples();
        expect(validExamples.length > 0).to.be.true;
      })
      it("must have invalid examples", function() {
        var invalidExamples = schema.getInvalidExamples();
        expect(invalidExamples.length > 0).to.be.true;
      })
      describe("example", function(){
        var validExamples = schema.getValidExamples();
        var invalidExamples = schema.getInvalidExamples();
        validExamples.forEach(function(validExample){
          describe("which is valid", function(){
            it("must be valid", function(){
              expect(schema.isValid(validExample)).to.be.true
            })
          })
        })
        invalidExamples.forEach(function(invalidExample){
          describe("which is invalid", function(){
            it("must be invalid", function(){
              expect(schema.isValid(invalidExample)).to.be.false
            })
          })
        })
        validExamples.forEach(function(validExample){
          invalidExamples.forEach(function(invalidExample){
            it("must not be valid and invalid", function(){
              expect(validExample).to.not.equal(invalidExample)
            })
          })
        })
      })
      it("must have a schema id", function() {
        expect(schema.getSchema()).to.have.a.property("id");
      })
    })
  })
})


