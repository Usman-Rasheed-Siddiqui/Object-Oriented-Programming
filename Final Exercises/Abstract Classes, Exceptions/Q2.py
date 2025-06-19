from abc import ABC, abstractmethod


class Polygon(ABC):
    def __init__(self):
        self.__no_of_sides = 3
        self.__lengths = []

    @property
    def no_of_sides(self):
        return self.__no_of_sides

    @no_of_sides.setter
    def no_of_sides(self, n):
        if isinstance(n, int) and n >= 3:
            self.__no_of_sides = n

    @property
    def lengths(self):
        return self.__lengths

    @lengths.setter
    def lengths(self, l):
        if isinstance(l, list) and len(l) == self.__no_of_sides and all(isinstance(item, (int, float)) for item in l):
            self.__lengths = l

    def perimeter(self):
        sum_length = sum(self.__lengths)
        return sum_length

    @abstractmethod
    def area(self):
        pass


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self)
        self.__no_of_sides = 4

    @property
    def lengths(self):
        return self.__lengths

    @lengths.setter
    def lengths(self, l):
        try:
            if isinstance(l, list) and len(l) == 2 and (isinstance(item, (int, float)) for item in l):
                self.__lengths = l
            else:
                raise OverflowError
        except OverflowError:
            print("Please provide 2 values i.e. Breath and Length")

    def perimeter(self):
        sum_length = 0
        for length in self.__lengths:
            sum_length += 2 * length

        return sum_length

    def area(self):
        return self.__lengths[0] * self.__lengths[1]


class RightTriangle(Polygon):
    def __init__(self):
        Polygon.__init__(self)

    @property
    def lengths(self):
        return self.__lengths

    @lengths.setter
    def lengths(self, l):
        try:
            if isinstance(l, list) and len(l) == 2 and all(isinstance(item, (int, float)) for item in l):
                self.__lengths = l
                hypotenuse = (self.__lengths[0] ** 2 + self.__lengths[1] ** 2) ** (1 / 2)
                self.__lengths.append(hypotenuse)
            else:
                raise IndexError

        except IndexError:
            print("Please provide 2 values i.e. Breath and Length")
            self.__lengths = None

    def area(self):

        return f"{1 / 2 * self.__lengths[0] * self.__lengths[1]} square units"


r = RightTriangle()
try:
    r.lengths =[1, 4, 3]
    if r.lengths:
        print(r.area())

except TypeError:
    print("Please provide 2 values i.e. Breath and Length")
