
from abc import ABC, abstractmethod

class Polygon(ABC):
    def __init__(self):
        self.no_of_sides = 3
        self.lengths = []

    def set_no_of_sides(self, n):
        if isinstance(n, int) and n >= 3:
            self.no_of_sides = n

    def set_lengths(self, l):
        if isinstance(l, list) and len(l) == self.no_of_sides and all(isinstance(item, (int,float)) for item in l):
            self.lengths = l

    def perimeter(self):
        sum_length = sum(self.lengths)
        return sum_length

    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self)
        self.set_no_of_sides(4)

    def set_lengths(self, l):
        try:
            if isinstance(l, list) and len(l) == 2 and (isinstance(item, (int,float)) for item in l):
                self.lengths = l
            else:
                raise OverflowError
        except OverflowError:
            print("Please provide 2 values i.e. Breath and Length")

    def perimeter(self):
        sum_length = 0
        for length in self.lengths:
            sum_length += 2*length

        return sum_length

    def area(self):
        return self.lengths[0] * self.lengths[1]


class RightTriangle(Polygon):
    def __init__(self):
        Polygon.__init__(self)

    def set_lengths(self, l):
        try:
            if isinstance(l, list) and len(l) == 2 and all(isinstance(item, (int,float)) for item in l):
                self.lengths = l
                hypotenuse = (self.lengths[0]**2 + self.lengths[1]**2)**(1/2)
                self.lengths.append(hypotenuse)
                return True
            else:
                raise IndexError

        except IndexError:
            print("Please provide 2 values i.e. Breath and Length")
            return False


    def area(self):

        return f"{1/2 * self.lengths[0] * self.lengths[1]} square units"

r = RightTriangle()
try:
    if r.set_lengths([1,2]):
        print(r.area())

except TypeError:
    print("Please provide 2 values i.e. Breath and Length")
    