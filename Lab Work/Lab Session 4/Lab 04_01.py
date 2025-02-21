
class Person:
    def __init__(self, name=''):
        self.name = name

    def showName(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name='', dept='', year=0000):
        super().__init__(name)
        self.department = dept
        self.year = year

    def showName(self):
        super().showName()
        print(f"Department: {self.department}")
        print(f"Year: {self.year}")

class Teacher(Person):
    def __init__(self, name='', course=''):
        super().__init__(name)
        self.course = course

    def showName(self):
        super().showName()
        print(f"Course: {self.course}")

p1 = Person("Ali")
p1.showName()
p2 = Student("Usman", "CIS Department", 2024)
p2.showName()
p3 = Teacher("Ahmed", "Functional English")
p3.showName()


