#!/usr/bin/python3
import os
import json
import sys
from pprint import pprint

if len(sys.argv) == 1:
    def choose_schema(schema):
        return True
else:
    valid_schemas = sys.argv[1:]
    def choose_schema(schema):
        return schema in valid_schemas

HERE = os.path.dirname(__file__) or "."
SCHEMAS = os.path.join(HERE, "..")
# add schemas to test below
schemas = {
    "curriculum" : os.path.join(SCHEMAS, "curriculum", "curriculum.json"),
    "resource" : os.path.join(SCHEMAS, "resource", "resource.json"),
    "search-response" : os.path.join(SCHEMAS, "search-response", "search-response.json"),
    "error" : os.path.join(SCHEMAS, "error", "error.json"),
}

try:
    import jsonschema
except:
    print("You may want to install the packages mentioned in requirements.txt.")
    raise

def schema_works(schema, instance):
    jsonschema.validate(instance, schema)

def schema_fails(schema, instance):
    try:
        jsonschema.validate(instance, schema)
        assert False, "Schema worked"
    except jsonschema.exceptions.ValidationError:
        pass
        
def load_json_from_file(file_name):
    try:
        with open(os.path.join(file_name), encoding="UTF-8") as f:
            return json.load(f)
    except ValueError:
        print(file_name)
        raise
        
def test_files(name, case):
    dir = os.path.join(SCHEMAS, name, "examples", case)
    files = [os.path.join(dirpath, file)
             for dirpath, dirnames, filenames in os.walk(dir)
             for file in filenames]
    return files

def test_schema(name, schema, message):
    works = test_files(name, "valid")
    fails = test_files(name, "invalid")
    for validate, files in [(schema_works, works), (schema_fails, fails)]:
        for file in files:
            instance = load_json_from_file(file)
            new_schema_calls()
            try:
                validate(schema, instance)
            except:
                print("file:", file)
                print("schema:", schema)
                print("instance:", instance)
                for call in schema_calls:
                    print(*call)
                raise
            else:
                print(message, "| ok", file)
    assert works, "schema " + name + " should test a valid example"
    assert fails, "schema " + name + " should test an invalid example"

schema_calls = []
def new_schema_calls():
    global schema_calls
    schema_calls = []

def execute_tests(name, schema):
    test_schema(name, schema, name + " as schema")

def main():
    for name, path in schemas.items():
        if choose_schema(name):
            schema = load_json_from_file(path)
            schema["id"] = "file://" + os.path.abspath(path).replace("\\", "/")
            execute_tests(name, schema)
        else:
            print("SKIP", name)

main()
