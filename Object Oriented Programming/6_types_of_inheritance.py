#Program showcasing different types of inheritance in Python
#Single Inheritance: A class inherits from one parent class
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def bark(self):
        return "Dog barks"
dog = Dog()
print(dog.speak()) #Inherited from Animal
print(dog.bark())  #Defined in Dog

#Multiple Inheritance: A class inherits from more than one parent class
class Flyer:
    def fly(self):
        return "Flying"
class Swimmer:
    def swim(self):
        return "Swimming"
class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack"
    
duck = Duck()
print(duck.fly())   #Inherited from Flyer
print(duck.swim())  #Inherited from Swimmer
print(duck.quack()) #Defined in Duck

#Multilevel Inheritance: A class inherits from a derived class
class Vehicle:
    def start(self):
        return "Vehicle started"
class Car(Vehicle):
    def drive(self):
        return "Car is driving"
class SportsCar(Car):
    def turbo(self):
        return "Turbo mode on"
sports_car = SportsCar()
print(sports_car.start())  #Inherited from Vehicle
print(sports_car.drive())  #Inherited from Car
print(sports_car.turbo())  #Defined in SportsCar

#Hierarchical Inheritance: Multiple classes inherit from a single parent class
class Shape:
    def area(self):
        return "Calculating area"
class Circle(Shape):
    def area(self):
        return "Area of Circle"
class Square(Shape):
    def area(self):
        return "Area of Square"
circle = Circle()
square = Square()
print(circle.area()) #Area of Circle
print(square.area()) #Area of Square

#Hybrid Inheritance: A combination of two or more types of inheritance
class A:
    def method_a(self):
        return "Method A"
class B(A):
    def method_b(self):
        return "Method B"
class C(A):
    def method_c(self):
        return "Method C"
class D(B, C):
    def method_d(self):
        return "Method D"
d = D()
print(d.method_a()) #Inherited from A
print(d.method_b()) #Inherited from B
print(d.method_c()) #Inherited from C
print(d.method_d()) #Defined in D

# super keyword showcase by sending value to parent class variable
class Parent:
    def __init__(self, name):
        self.name = name
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  #Calling Parent class constructor
        self.age = age
child = Child("Umar", 20)
print(child.name) #Inherited from Parent
print(child.age)  #Defined in Child

# Multiple inheritance can lead to the "Diamond Problem," which can be resolved using the Method Resolution Order (MRO) in Python which is basically
# the order in which base classes are searched when executing a method. Python uses the C3 linearization algorithm to determine the MRO.
# It means that Python will look for a method in the current class first, then in the parent classes from left to right as they are defined in the class declaration.
class X:
    def show(self):
        return "X"
class Y(X):
    def show(self):
        return "Y"
class Z(X):
    def show(self):
        return "Z"
class A(Y, Z):
    pass
a = A()
print(a.show()) #Output will be Y because of MRO (A -> Y -> Z -> X)
print(A.mro()) #Shows the method resolution order
 