var expect = require("chai").expect
var api = require("../lib/main.js")

describe("Schemas", function(){
  describe("attributes", function() {
    it("must contain resource and error schema", function() {
      expect(api).to.have.a.property("resource")
      expect(api).to.have.a.property("error")
    })
  })
})


