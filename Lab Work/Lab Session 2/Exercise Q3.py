
class Student:
    def __init__(self, Name="John",batch="2022",year="Final year"):
        self.name = Name
        print(self.name)
        self.batch = batch
        print(self.batch)
        self.year = year
        print(self.year)

    def __int__(self):
        print("Empty object created")

c1= Student()

# The first __init__ method will be executed. This is because __init__ default constructor can only be created once.
# As a result only the first instance of the functon will be called. The second one will not be executed.

# OUTPUT:
#John
#2022
#Final year
