
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height
        print(f"Area = {self.area} square units")

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

S1 = Square(12)