#Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object.
#It helps in reducing programming complexity and effort.
#In Python, abstraction can be achieved using abstract classes and methods provided by the 'abc' module.
#Abstract classes and methods are basically classes and methods that are declared but contain no implementation.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod #Decorator to declare an abstract method
    def make_sound():
        pass #Pass indicates that the method has no implementation

class Dog(Animal):
    def make_sound(self):
        print("Woof")

d = Dog()
d.make_sound()

#If we try to create an instance of the abstract class Animal, it will raise an error
#In this example we have defined an abstract class Animal with an abstract method make_sound.
#The Dog class inherits from Animal and provides an implementation for the make_sound method.
#When we create an instance of Dog and call the make_sound method, it prints "Woof".
#If we had not implemented the make_sound method in the Dog class, trying to create an instance of Dog would have raised a TypeError.
#Abstract classes are useful when you want to define a common interface for a group of related classes.
