#Inheritance is basically a new class derived from an existing class which will contain all the features of the parent class.
class Employee:
    start = 9
    end = 5

    def change_time(self, start, end):
        self.start = start
        self.end = end

class teacher(Employee):
    def __init__(self, name):
        self.name = name

t1 = teacher("Umar")
print(t1.name, t1.start, t1.end)
t1.change_time(8, 4)
print(t1.start, t1.end)