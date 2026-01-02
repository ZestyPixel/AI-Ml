import json

json_str = '{"name": "Umar", "isStudent": true}' # JSON string converted to Python object
#These are to deal with strings.
py_ob = json.loads(json_str)
print(py_ob)
py_str = json.dumps(py_ob) # Python object converted to JSON string
print(py_str)

