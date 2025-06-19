
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def set_x(self):
        try:
            self.x = int(input("Enter x coordinate: "))
        except ValueError:
            print("Please enter valid integer")

    def set_y(self):
        try:
            self.y = int(input("Enter y coordinate: "))
        except ValueError:
            print("Please enter valid integer")

    def __str__(self):
        return self.x, self.y

class LineSegment:
    def __init__(self):
        self.point1 = Point()
        self.point2 = Point()
        self.set_point1()
        self.set_point2()

    def set_point1(self):
        self.point1.set_x()
        self.point1.set_y()

    def set_point2(self):
        self.point2.set_x()
        self.point2.set_y()

    def findLength(self):
        self.length = ((self.point1.x - self.point2.x)**2 + (self.point1.y - self.point2.y)**2)**0.5
        return self.length

    def __gt__(self, length2):
        return self.length > length2.length

# L1 = LineSegment()
# L2 = LineSegment()
# L1.findLength()
# print(L1.length)
# L2.findLength()
# print(L2.length)
# print(L1 > L2)

#Q7
# class DistanceFinder(Point):
#     def findDistance(self, p):
#         distance = ((self.x - p.x)**2 + (self.y - p.y)**2)**0.5
#         return round(distance, 3)

class DistanceFinder(Point):

    @staticmethod
    def findDistance(p1, p2):
        distance = ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5
        return round(distance, 3)

D1 = DistanceFinder()
D1.set_x()
D1.set_y()

D2 = DistanceFinder()
D2.set_x()
D2.set_y()
print(D1.findDistance(D1, D2))

