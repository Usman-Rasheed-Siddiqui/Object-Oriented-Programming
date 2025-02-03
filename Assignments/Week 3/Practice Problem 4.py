
class Vehicle:

    def __init__(self):
        self.setName(input("Enter name of vehicle: "))
        self.setMax_Speed(input("Enter max speed of vehicle: "))
        self.setSeats(int(input("Enter number of seats: ")))
        self.setMileage(float(input("Enter mileage of vehicle: ")))
        self.setColor(input("Enter color of vehicle: "))

    def setName(self, name):
        self.name = name

    def setMax_Speed(self, max_speed):
        self.max_speed = max_speed

    def setSeats(self, seats):
        self.seats = seats

    def setMileage(self, mileage):
        self.mileage = mileage

    def setColor(self, color = "White"):
        self.color = color

    def getName(self):
        return self.name

    def getMax_Speed(self):
        return self.max_speed

    def getSeats(self):
        return self.seats

    def getMileage(self):
        return self.mileage

    def getColor(self):
        return self.color

    def seating_capacity(self):
        print("Name of Vehicle:",self.name)
        print("Number of Seats:",self.seats)

    def find_fare(self):
        return self.seats * 100

NewVehicle = Vehicle()
print("Max Speed:",NewVehicle.getMax_Speed(), "km\\h")
NewVehicle.seating_capacity()
print("Fare of Vehicle:",NewVehicle.find_fare(),"PKR")