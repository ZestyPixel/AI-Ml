class Student:
    college = "College: Amity University" #This is a class attribute, shared by all instances of the class.

    def __init__(self, name, cgpa):
        self.name = name #This is an instance attribute, unique to each instance of the class.
        self.cgpa = cgpa

    def get_details(self):
        print(f"Name: {self.name}, CGPA: {self.cgpa}")
    
stud1 = Student("Umar", 5.94)
stud1.get_details()
print(Student.college)
