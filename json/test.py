# JSON linter
# https://jsonlint.com/

import json

person_dict = {"first": "John", "last": "doe"}
person_dict["city"] = "Somewhere"

# converts Python to JSON string (literal)
person_json_str = json.dumps(person_dict)
# {"first": "John", "last": "doe", "city": "Somewhere"}
print(person_json_str)
print(person_json_str[0])
print(person_json_str[8])
index = person_json_str.find("last")
print(index)
print(person_json_str[index])
print("----------")

person_dict["languages"] = ["Python", "C++", "Rust", "Go", "Java", "Javascript"]
person_dict["contacts"] = {
    "email": "none@none.com",
    "office": "+1 (312) 555-1212",
    "mobile": "+1 (312) 555-2121",
}
print("person (dict) --> {}".format(person_dict))


person_json_str = json.dumps(person_dict)
# converts JSON string (parses it) to JSON object
person_json_obj = json.loads(person_json_str)
print("languages --> {}".format(person_json_obj["languages"]))
print("email --> {}".format(person_json_obj["contacts"]["email"]))
print("person (json) --> {}".format(person_json_obj))
print("all languages:")
# Python
# C++
# Rust
# Go
# Java
# Javascript
for item in person_json_obj["languages"]:
    print(item)
print("----------")

staff_dict = {}
staff_dict["Manager"] = person_dict
staff_json_str = json.dumps(staff_dict)
# {"Manager": {"first": "John", "last": "doe", "city": "Somewhere"}}
#
# {
# 	"Manager": {
# 		"first": "John",
# 		"last": "doe",
# 		"city": "Somewhere",
# 		"languages": ["Python", "C++", "Rust", "Go", "Java", "Javascript"]
# 	}
# }
print(staff_json_str)
