class Student:
    name = ""
    # def __init__(self): No function overloading in python, so cannot make more than one constructor as the last one will be the only valid one
    #     print("Object Created")
        
    def __init__(self, name, cgpa): #Here self is a reference to the current instance of the class meaning the object that is being created.
        self.name = name #These are instance variables while the ones outside are class variables.
        self.cgpa = cgpa
        print(self.name)
        
    def get_cgpa(self):
        print(self.cgpa)

stud1 = Student("Umar", 5.94)
stud1.get_cgpa()