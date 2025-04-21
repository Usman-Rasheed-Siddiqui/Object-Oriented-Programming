
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height
        print(f"Area of the Rectangle = {self.area} square units")

R1 = Rectangle(30, 45)