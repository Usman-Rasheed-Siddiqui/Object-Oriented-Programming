class Point:
    def __init__(self):
        self.setx()
        self.sety()

    def setx(self):
        self.xcoord = int(input("Enter x coordinate: "))

    def sety(self):
        self.ycoord = int(input("Enter y coordinate: "))

    def getCoordinates(self):
        return (self.xcoord, self.ycoord)

    def move(self, dx, dy):
        self.xcoord += dx
        self.ycoord += dy

Pts = Point()
print(Pts.getCoordinates())
Pts.move(int(input("Enter x coordinate to move: ")),int(input("Enter y coordinate to move: ")))
print(Pts.getCoordinates())