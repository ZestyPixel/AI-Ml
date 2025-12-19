#Print all the unique subjects, students enrolled in english and create dictionary(student, set of courses)
info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

unique_courses = set()
for tup in info:
    unique_courses.add(tup[1])

print(unique_courses)

for name, course in info:
    if course == "English":
        print(name)

dict = {}

for name, course in info:
    if dict.get(name) == None:
        dict.update({
            name: set()
        })
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict.items())