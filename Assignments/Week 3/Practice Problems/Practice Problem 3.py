
class Circle:
    '''Class to set circle properties and to get it'''
    def __init__(self):
        self.setRadius(int(input("Enter the radius of the circle: ")))  # Take input for radius and set it
        self.setColor(input("Enter the color of the circle: "))  # Take input for color and set it

    def setRadius(self, radius):
        '''Set the radius of the circle'''
        self.radius = radius

    def setColor(self, color):
        '''Set the color of the circle'''
        self.color = color

    def getRadius(self):
        '''Get the radius of the circle'''
        return self.radius

    def getColor(self):
        '''Get the color of the circle'''
        return self.color

    def Circumference(self):
        '''Calculate the circumference of the circle'''
        return round(2*(22/7)*self.radius, 2)

    def Area(self):
        '''Calculate the area of the circle'''
        return round((22/7)*self.radius**2, 2)

NewCircle = Circle()    # Creating an instance of the class Circle
NewCircle.getRadius()
NewCircle.getColor()
print(f"Circumference: {NewCircle.Circumference()} units")      # Printing calculated Circumference
print(f"Area: {NewCircle.Area()} square units")     # Printing calculated Area

NewCircle2 = Circle()    # Creating an instance of the class Circle
NewCircle2.getRadius()
NewCircle2.getColor()
print(f"Circumference: {NewCircle2.Circumference()} units")      # Printing calculated Circumference
print(f"Area: {NewCircle2.Area()} square units")     # Printing calculated Area