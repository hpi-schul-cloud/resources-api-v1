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
    "curriculum" : os.path.join(SCHEMAS, "curriculum", "curriculum.json")
}

try:
    import jsonschema
    checker = jsonschema.FormatChecker(("date-time",))
except:
    print("You may want to install the packages mentioned in requirements.txt.")
    raise

def schema_works(schema, instance):
    jsonschema.validate(instance, schema, format_checker=checker)

def schema_fails(schema, instance):
    try:
        jsonschema.validate(instance, schema, format_checker=checker)
        assert False, "Schema worked"
    except jsonschema.exceptions.ValidationError:
        pass
        
def load_json_from_file(file_name):
    try:
        with open(os.path.join(HERE, file_name)) as f:
            return json.load(f)
    except ValueError:
        print(file_name)
        raise
        
def test_files(name, case):
    dir = os.path.join(SCHEMAS, name, "tests", case)
    return [os.path.join(dirpath, file)
            for dirpath, dirnames, filenames in os.walk(dir)
            for file in filenames]

def test_schema(name, schema, message):
    """Test a schema against all files starting with `name`
    
    - name_works.json files are expected to be valid
    - name_fails.json files are expected to be invalid
    """
    works = test_files(name, "works")
    fails = test_files(name, "fails")
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
                print("checkers:", checker.checkers)
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

for name, path in schemas.items():
    if choose_schema(name):
        schema = load_json_from_file(path)
        execute_tests(name, schema)
    else:
        print("SKIP", name)