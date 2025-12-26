class Person:
    def __init__(self, name, age = "None", address = ""):
        self.name = name
        self.age = age
        self.address = address

person1 = Person("Alice")
person2 = Person("Bob", 30)
person3 = Person("Charlie", 25, "123 Main St")