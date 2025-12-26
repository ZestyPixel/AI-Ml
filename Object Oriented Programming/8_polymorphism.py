#Polymorphism in python allows methods to do different things based on the object it is acting upon, even if they share the same name.
#This means that a single function or method can work in different ways depending on the context in which it is used.
#We cannot perform method overloading in python like other languages such as Java or C++. 
# In those languages, you can define multiple methods with the same name but different parameters within the same class.
#However, Python does not support this feature directly. 
# If you define multiple methods with the same name in a class, the last definition will overwrite the previous ones.
# However, we can achieve similar functionality using default arguments or variable-length arguments.
#The two types of polymorphism in Python are function overriding, duck typing, operator overloading, function polymorphism(built in).
#Function Overriding: When a subclass provides a specific implementation of a method that is already defined in its superclass.
#Duck Typing: An object's suitability is determined by the presence of certain methods and properties, rather than the actual type of the object.

#Function overriding
class Employee:
    def get_designation(self):
        print("Employee")
class Developer(Employee):
    def get_designation(self):
        print("Developer")

d = Developer()
d.get_designation()

#Operator overloading
class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

v1 = Vector(10)
v2 = Vector(20)
print(v1 + v2)

#Duck typing: If it walks like a duck, quacks like a duck, it is a duck.
#In layman terms, it means that we do not check the type of an object to determine if it can be used for a particular purpose.
#Instead, we check if it has the necessary methods and properties.
#In this example, both Cat and Dog classes have a sound method.
#We can use both objects interchangeably in the same context without worrying about their actual types.

class Dog:
    def speak(self):
        return "Bark"

class Human:
    def speak(self):
        return "Hello"

def make_sound(obj):
    print(obj.speak())

d = Dog()
h = Human()
make_sound(d)
make_sound(h)
