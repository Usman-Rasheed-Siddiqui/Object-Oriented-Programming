
# Default Constructor
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

# Non parameterized constructor:
# class complex_number:
#     def __init__(self):               # self ensures that the c1 real and imaginary no. do not get mixed up with another object
#         self.real = int(input("Enter real part: "))
#         self.img = int(input("Enter imaginary part: "))
#         #self.real = 0
#         #self.img = 0
#
#     def print_complex(self):
#         print(f"Complex number: {self.real} + {self.img}j" )
#
# c1 = complex_number()
# c1.print_complex()

# Parameterized constructor:
# class complex_number:
#     def __init__(self, real, img):  # self ensures that the c1 real and imaginary no. do not get mixed up with another object
#         self.real = real
#         self.img = img
#         # self.real = 0
#         # self.img = 0
#
#     def print_complex(self):
#         print(f"Complex number: {self.real} + {self.img}j")
#
# c1 = complex_number(5,8)
# c1.print_complex()

# Parameterized constructor with default values (Parameterized constructor that works like a default constructor)
# class complex_number:
#     def __init__(self, real=0, img=0):  # self ensures that the c1 real and imaginary no. do not get mixed up with another object
#         self.real = real
#         self.img = img
#         # self.real = 0
#         # self.img = 0
#
#     def print_complex(self):
#         print(f"Complex number: {self.real} + {self.img}j")
#
# c1 = complex_number()
# c1.print_complex()
# c2 = complex_number(7,5)
# c2.print_complex()
# c3 = complex_number(7)
# c3.print_complex()
# c4 = complex_number(img=8)
# c4.print_complex()