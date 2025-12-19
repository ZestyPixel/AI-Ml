#Unordered, key value pairs

dict = {
    "name" : "Umar",
    1: "Hello World",
    "list": [1,2,3],
    2: "Hello"
}

dict[2] = "Halo"

print(dict[2])
print(dict.keys())
print(list(dict.values()))
print(dict.items())
print(dict.get("name"))
dict.update({
    "city": "Delhi"
})
print(dict.items())




