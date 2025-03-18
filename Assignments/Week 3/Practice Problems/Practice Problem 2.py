
class Student:
    '''Class to check on a student'''
    def __init__(self):
        self.setName(input("Enter your name: "))
        self.setRoll(input("Enter your roll number: "))
        self.marks = [0,0,0]
        self.setMarks()

    def setName(self,name=None):
        '''Sets the name of the student'''
        self.name = name

    def setRoll(self, roll=None):
        '''Sets the roll number of the student'''
        self.roll = roll

    def setMarks(self):
        '''Sets the marks of three quizzes of the student'''
        for i in range(1,4):
            self.mark = int(input(f"Enter your marks for quiz {i}: "))
            self.marks[i-1] = self.mark

    def getName(self):
        '''Get the name of the student'''
        return self.name

    def getRoll(self):
        '''Get the roll number of the student'''
        return self.roll

    def getMarks(self):
        '''Get the marks of three quizzes of the student'''
        return self.marks

    def getStudent(self):
        '''Print the student's information'''
        print("Student:",self.name)
        print("Roll Number:",self.roll)
        print("Marks:")
        for i in range(1, len(self.marks)+1):
            print(f"Quiz{i}", self.marks[i-1])

    def avg(self):
        '''Get average of three quizzes of the student'''
        return sum(self.marks)/len(self.marks)

Std = Student()     # Creating an instance of the class
Std.getName()       # To get the name of the student
Std.getRoll()       # To get the roll number of the student
Std.getMarks()      # To get the marks of 3 quizzes of the student
Std.getStudent()    # Print student's info
print("Average of 3 quizzes:",Std.avg())           # Prints average of the three quizzes

Std2 = Student()     # Creating an instance of the class
Std2.getName()       # To get the name of the student
Std2.getRoll()       # To get the roll number of the student
Std2.getMarks()      # To get the marks of 3 quizzes of the student
Std2.getStudent()    # Print student's info
