# Encapsulation in Object Oriented Programming refers to the bundling of data (attributes) and methods (functions) that operate on that data within a single unit 
# or class.
# It restricts direct access to some of the object's components, which is a means of preventing unintended interference and misuse of the methods and data.
# In Python, encapsulation is implemented using access specifiers: public, protected, and private

# Now access specifiers are not enforced by the Python interpreter except for private members, but they are a convention to indicate the intended level of access.

class bankAccount:
    def __init__(self, name, balance, number):
        self.name = name #Public attribute, accessible inside and outside the class
        self._balance = balance #Protected can only be accessed within the class and its subclasses but not from outside the class. It is not enforced by Python.
        self.__number = number #Private attribute with name mangling, not accessible from outside the class

    def get_account_number(self): #Getter method to access private attribute
        return self.__number
    
    def set_account_number(self, new_number): #Setter method to update private attribute
        self.__number = new_number


umar = bankAccount("Umar", 5000, "1234567890")
print(umar.name) #Accessing public attribute
print(umar._balance) #Even though this is accessible, it is a convention to indicate that it should not be accessed directly from outside the class
#print(umar.__number) This will result in error because number is private
print(umar._bankAccount__number) #Here we are accessing private attribute using name mangling, but this is not recommended. 
#Name mangling: In Python, when you make an attribute private, the interpreter changes the name of the attribute in a way that makes it harder to create subclasses that accidentally override the private attributes and methods.
#but still it can be accessed using objectName._ClassName__privateAttribute
