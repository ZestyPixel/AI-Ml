class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod #This is a decorator to define a class method. Decorators are a way to modify the behavior of functions or methods.
    def get_storage_type(cls): #This is a class method because it takes cls as the first parameter. Cls methods cannot access instance attributes directly. 
        print(cls.storage_type)

    def get_specs(self): #This is a instance method because it takes self as the first parameter.
        print(f"RAM: {self.RAM}, Storage: {self.storage} ({Laptop.storage_type})")

    @staticmethod #This is a static method decorator. Static methods do not take self or cls as the first parameter. They behave like regular functions but belong to the class's namespace.
    def calc_cost(units, price): #They behave like regular functions but belong to the class's namespace.
        print("Cost: ", units*price)

laptop = Laptop("16GB", "1TB")
laptop.get_specs() #Calling instance method
Laptop.get_storage_type() #Calling class method
Laptop.calc_cost(2, 500) #Calling static method


