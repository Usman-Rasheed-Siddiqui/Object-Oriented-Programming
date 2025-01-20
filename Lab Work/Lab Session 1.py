
"OOP is about creating objects that contain both data and functions"

"CLASS: template for object. Are abstract"
"OBJECT: An instance of a class"
" Three characteristics"
"   -Attributes"
"   -Function"
"   -Identity"

# Question 2

#Method 1
# class complex_number:
#     def take_input(self):               # self ensures that the c1 real and imaginary no. do not get mixed up with another object
#         self.real = int(input("Enter real part: "))
#         self.img = int(input("Enter imaginary part: "))
#
#     def print_complex(self):
#         print(f"Complex number: {self.real} + {self.img}j" )
#
# c1 = complex_number()
# c1.take_input()
# c1.print_complex()

# #Method 2
# class complex_number2:                  # self ensures that the c2 real and imaginary no. do not get mixed up with c3
#     def take_input(self, r, i):
#         self.real = r
#         self.img = i
#
#     def print_complex(self):
#         print(f"Complex number: {self.real} + {self.img}j" )
#
# c2 = complex_number2()
# c2.take_input(5,7)
# c2.print_complex()
#
# c3 = complex_number2()
# c3.take_input(9,8)
# c3.print_complex()

# Question 1
# class Bank:
#     def set_loan(self, v):      # Set value of loan
#         self.loan_take_previously = v
#
#     def application_for_loan(self):
#         if(self.loan_take_previously == True):
#             print("Loan not granted")
#         elif(self.loan_take_previously == False):
#             print("Loan granted")
#         else:
#             print("Invalid Entry")
#
# b1 = Bank()
# b1.set_loan(True)
# b1.application_for_loan()
# b1.loan_take_previously = 123      #Not a good approach
# b1.application_for_loan()
#
# b2 = Bank()
# b2.set_loan(False)
# b2.application_for_loan()

#Question 3
# class snake:
#     def introduction(self):
#         self.name = input("Enter name of the snake: ")
#         self.color = input("Enter snake's color: ")
#         self.age = input("Enter it's age: ")
#
#         print("Name: ", self.name)
#         print("Color: ", self.color)
#         print("Age: ", self.age)
#
# snake_class = snake()
# snake_class.introduction()

# Question 4:

# class car:
#     def attributes(self, v):
#         self.wheels = 4
#         self.miles = 5000
#         self.make = 'KIA'
#         self.model = 2024
#         self.year = 2025
#         self.sold_on = v
#
#     def sales_price(self):
#         if self.sold_on == None:
#             print("Sale Price = 0 PKR")
#         else:
#             print("Sale Price = 10,000,000 PKR")
#
#     def purchase_price(self):
#         if self.sold_on == None:
#             print("Sale Price = 0 PKR")
#         else:
#             print("Sale Price = 9,500,000 PKR")


# Class Exercise:
# class Student:
#
#     # For Name:
#     def set_name(self):
#         self.name = input("Enter student's name: ")
#     def get_name(self):
#         return self.name
#
#     # For Roll:
#     def set_roll(self):
#         self.roll = input("Enter student's roll no. : ")
#     def get_roll(self):
#         return self.roll
#
#     # For marks:
#     def set_marks(self):
#         self.marks = []
#         for i in range(1,4):
#             marks  = float(input(f"Enter marks for Quiz {i}: "))
#             self.marks.append(marks)
#     def get_marks(self):
#         return self.marks
#
#     def print_student(self):
#         print(f"Student Name: {self.get_name()} \n Roll No.: {self.get_roll()}")
#         for i in range(1,4):
#             print(f"Quiz{i}: {self.get_marks()[i-1]}")
#
#     def avg(self):
#         return sum(self.get_marks())/3
#
# student = Student()
# student.set_name()
# student.set_roll()
# student.set_marks()
# student.print_student()
# print("Average: ",student.avg())


