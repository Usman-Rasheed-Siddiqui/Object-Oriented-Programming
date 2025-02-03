
class Circle:
    def __init__(self):
        self.setRadius(int(input("Enter the radius of the circle: ")))
        self.setColor(input("Enter the color of the circle: "))

    def setRadius(self, radius):
        self.radius = radius

    def setColor(self, color):
        self.color = color

    def getRadius(self):
        return self.radius

    def getColor(self):
        return self.color

    def Circumference(self):
        return round(2*(22/7)*self.radius, 2)

    def Area(self):
        return round((22/7)*self.radius**2, 2)

NewCircle = Circle()
NewCircle.getRadius()
NewCircle.getColor()
print(f"Circumference: {NewCircle.Circumference()} units")
print(f"Area: {NewCircle.Area()} square units")


