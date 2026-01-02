#For files
import json

dict = {
    "name": "John Doe",
    "age" : 13,
}

with open("data.json", "r+") as f:
    py_obj = json.load(f)
    print(py_obj)
    json.dump(dict, f, indent=4, sort_keys=True)