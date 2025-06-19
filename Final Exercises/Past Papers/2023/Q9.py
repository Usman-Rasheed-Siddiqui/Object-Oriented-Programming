from abc import ABC, abstractmethod

class Shape_2D(ABC):
    def __init__(self, name = "2D_shape", dimensions = [0,0]):
        self.shape_type=name
        self.dimensions=dimensions

    @property
    @abstractmethod
    def SHAPE(self):
        """This is a shape_type abstract property"""
        pass

    @SHAPE.setter
    def SHAPE(self, name):
        self.shape_type=name
    
    @abstractmethod
    def find_area(self):
        #multiply first two dimensions stored in the list self.dimensions
        pass

    def find_perimeter(self):
        #adding all the dimensions stored in the list self.dimensions
        return sum(self.dimensions)

class Right_Triangle(Shape_2D):
    def __init__(self, name= "2D_shape", dimensions = [0,0,0]):
        super().__init__(name, dimensions)

    @property
    def SHAPE(self):
        return self.shape_type

    @SHAPE.setter
    def SHAPE(self, name):
        self.shape_type = name

    def find_area(self):
        return (1/2)*(self.dimensions[0]*self.dimensions[1])

R1 = Right_Triangle(dimensions=[1,4,1])
print(R1.find_area())
print(R1.find_perimeter())
print(R1.SHAPE)