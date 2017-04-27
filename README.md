# ressources-api-v1

The API specification to add content to the Schul-Cloud.
This is the [Ressources-=API form the architecture][arch]

If you like to work on this on bring in new ideas, you can open an issue and discuss with us.

## Structure

To verify your requests and responses, the is specified as follows:
- This README contains a complete description of
  - Objects 
    - with all attributes
    - their description
    - examples
    - points unclear that need to be specified, marked with a **TODO**
    - their dependencies on other attributes
  - endpoints
    - described like objects
- The `schema` folder contains the JSON-Schema to verify the different formats
- The `docker` folder contains a test-endpoint which can be used to test you application against.

## Endpoints

- TODO







## Further Reading
- [README Driven Development][rdd]

[rdd]: http://tom.preston-werner.com/2010/08/23/readme-driven-development.html
[arch]: https://schul-cloud.github.io/blog/2017-04-24/extensible-content-delivery#architecture