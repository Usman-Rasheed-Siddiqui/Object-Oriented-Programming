
class Student:
    def __init__(self):
        self.setName(input("Enter your name: "))
        self.setRoll(input("Enter your roll number: "))
        self.marks = [0,0,0]
        self.setMarks()

    def setName(self,name=None):
        self.name = name

    def setRoll(self, roll=None):
        self.roll = roll

    def setMarks(self):
        for i in range(1,4):
            self.mark = int(input(f"Enter your marks for quiz {i}: "))
            self.marks[i-1] = self.mark

    def getName(self):
        return self.name

    def getRoll(self):
        return self.roll

    def getMarks(self):
        return self.marks

    def getStudent(self):
        print("Student:",self.name)
        print("Roll Number:",self.roll)
        print("Marks:")
        for i in range(1, len(self.marks)+1):
            print(f"Quiz{i}", self.marks[i-1])

    def avg(self):
        return sum(self.marks)/len(self.marks)

Std = Student()
Std.getName()
Std.getRoll()
Std.getMarks()
Std.getStudent()
Std.avg()

