
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print("Name:",self.name)

    def print_age(self):
        print("Age:",self.age)

class Student:
    def __init__(self, student_id, roll_number):
        self.student_id = student_id
        self.roll_number = roll_number

class Resident(Person, Student):
    def __init__(self, name, age, student_id, roll_number):
        Person.__init__(self, name, age)
        Student.__init__(self, student_id, roll_number)

R1 = Resident("Usman", 19, 24038, 38)
R1.print_name()
R1.print_age()
