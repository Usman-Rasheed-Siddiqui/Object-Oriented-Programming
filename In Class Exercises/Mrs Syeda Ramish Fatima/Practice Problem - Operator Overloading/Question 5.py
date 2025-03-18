
class Point:
    '''Class to assign values to xy-coordinates'''
    def __init__(self, xcoord= 0, ycoord= 0):
        self.x = xcoord
        self.y = ycoord

    def setx(self):
        '''Sets the value of x coordinate'''
        self.x = int(input("Enter x coordinate: "))

    def sety(self):
        '''Sets the value of y coordinate'''
        self.y = int(input("Enter y coordinate: "))

    def getCoordinates(self):
        '''Returns the value of x and y as tuple'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''Moves the xy-coordinate by dx and dy'''
        self.x += dx
        self.y += dy


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1 if isinstance(p1,Point) else Point(0,0)
        self.p2 = p2 if isinstance(p2,Point) else Point(0,0)

    def __invert__(self):
        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y
        length = round((dx**2 + dy**2)**0.5, 2)
        return length

L1 = Line(Point(5,6), Point(6,7))
print("Length of line:",~L1, "units")