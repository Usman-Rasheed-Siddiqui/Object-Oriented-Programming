class Point:
    '''Class to assign values to xy-coordinates'''
    def __init__(self):
        self.setx()
        self.sety()

    def setx(self):
        '''Sets the value of x coordinate'''
        self.xcoord = int(input("Enter x coordinate: "))

    def sety(self):
        '''Sets the value of y coordinate'''
        self.ycoord = int(input("Enter y coordinate: "))

    def getCoordinates(self):
        '''Returns the value of x and y as tuple'''
        return (self.xcoord, self.ycoord)

    def move(self, dx, dy):
        '''Moves the xy-coordinate by dx and dy'''
        self.xcoord += dx
        self.ycoord += dy

Pts = Point()   # Assigned an object to the class
print(Pts.getCoordinates())     # Printing coordinates
Pts.move(int(input("Enter x coordinate to move: ")),int(input("Enter y coordinate to move: ")))
print(Pts.getCoordinates())