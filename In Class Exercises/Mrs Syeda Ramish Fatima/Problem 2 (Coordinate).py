
class Point:
    '''Class to assign values to xy-coordinates'''
    def __init__(self, xcoord= 0, ycoord= 0):
        self.__x = xcoord
        self.__y = ycoord

    def setx(self):
        '''Sets the value of x coordinate'''
        self.__x = int(input("Enter x coordinate: "))

    def sety(self):
        '''Sets the value of y coordinate'''
        self.__y = int(input("Enter y coordinate: "))

    def getCoordinates(self):
        '''Returns the value of x and y as tuple'''
        return (self.__x, self.__y)

    def move(self, dx, dy):
        '''Moves the xy-coordinate by dx and dy'''
        self.__x += dx
        self.__y += dy

P1 = Point()  # Assigned an object to the class
print(P1.getCoordinates())     # Printing coordinates
print(P1.__dict__)
print(Point.__dict__)

print(P1._Point__x)
P1.__x = 4
print(P1.__dict__)

P1._Point__x = 5
print(P1.__dict__)