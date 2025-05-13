
class Student:
    course_count = 0
    count = 0
    courses = {}

    def __init__(self, name="",roll="", email="", gpa=0):
        self.name = name
        self.roll_number = roll
        self.email_address = email
        self.student_courses = {}
        self.all_gpa = []

    @classmethod
    def course_info(cls):
        cls.course_count = int(input("Enter course count: "))
        cls.count = 0
        cls.courses = {}

    def input_info(self):
        self.name = input("Enter your name: ")
        self.roll_number = input("Enter your roll number: ")
        self.email_address = input("Enter your email address: ")

    @classmethod
    def add_course(cls):
        if cls.count == cls.course_count:
            print("You have already added the required number of courses.")
        else:
            course_name = input("Enter course name: ")
            cls.courses[course_name] = Student.GPA_calculator()
            cls.count += 1

    @staticmethod
    def GPA_calculator():
        gpa = 0
        marks= float(input("Enter your marks: "))

        if 100 >= marks >= 85:
            gpa = 4.0
        elif 84 >= marks >= 80:
            gpa = 3.7
        elif 79 >= marks >= 75:
            gpa = 3.4
        elif 74 >= marks >= 70:
            gpa = 3.0
        elif 69 >= marks >= 67:
            gpa = 2.7
        elif 66 >= marks >= 64:
            gpa = 2.4
        elif 63 >= marks >= 60:
            gpa = 2.0
        return gpa

    def CGPA_calculator(self):

        self.student_courses = Student.courses.copy()
        for gpa in self.courses.values():
            self.all_gpa.append(gpa)

        cgpa = sum(self.all_gpa) / len(self.all_gpa)
        print(f"The CGPA of {self.name} with Roll No. {self.roll_number} is:",round(cgpa,2))

student1 = Student()
student1.input_info()
student1.course_info()
Student.add_course()
Student.add_course()
Student.add_course()
student1.CGPA_calculator()