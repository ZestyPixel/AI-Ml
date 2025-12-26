class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    def set_name(self, name):
        if name.strip() == "":
            raise ValueError("Name cannot be empty")
        self.__name = name

    def get_name(self):
        print(self.__name)

    def set_roll_no(self, roll_no):
        if not (1 <= roll_no <= 100):
            raise ValueError("Roll number must be between 1 and 100")
        self.__roll_no = roll_no

    def get_roll_no(self):
        print(self.__roll_no)

    def set_marks(self, marks):
        if marks < 0:
            raise ValueError("Marks cannot be negative")
        self.__marks = marks

    def get_marks(self):
        print(self.__marks)

s1 = Student("Umar", 10, 95)
s1.get_name()
s1.get_roll_no()
s1.get_marks()
