
class Vehicle:
    '''Class to represent vehicle'''
    def __init__(self):
        self.setName(input("Enter name of vehicle: "))      # Input and set Vehicle name
        self.setMax_Speed(input("Enter max speed of vehicle: "))    # Input and set Max Speed
        self.setSeats(int(input("Enter number of seats: ")))    # Input and set Seats
        self.setMileage(float(input("Enter mileage of vehicle: ")))     # Input and set Mileage
        self.setColor(input("Enter color of vehicle: "))        # Input and set Color of Vehicle

    def setName(self, name):
        '''Sets name of the vehicle'''
        self.name = name

    def setMax_Speed(self, max_speed):
        '''Sets max speed of the vehicle'''
        self.max_speed = max_speed

    def setSeats(self, seats):
        '''Sets number of seats of the vehicle'''
        self.seats = seats

    def setMileage(self, mileage):
        '''Sets mileage of the vehicle'''
        self.mileage = mileage

    def setColor(self, color = "White"):
        '''Sets color of the vehicle'''
        self.color = color

    def getName(self):
        '''Returns name of the vehicle'''
        return self.name

    def getMax_Speed(self):
        '''Returns max speed of the vehicle'''
        return self.max_speed

    def getSeats(self):
        '''Returns number of seats of the vehicle'''
        return self.seats

    def getMileage(self):
        '''Returns mileage of the vehicle'''
        return self.mileage

    def getColor(self):
        '''Returns color of the vehicle'''
        return self.color

    def seating_capacity(self):
        '''Prints seating capacity of the vehicle and it's name'''
        print("Name of Vehicle:",self.name)
        print("Number of Seats:",self.seats)

    def find_fare(self):
        '''Returns fare of the vehicle'''
        return self.seats * 100

NewVehicle = Vehicle()      # Create instance of vehicle
print("Max Speed:",NewVehicle.getMax_Speed(), "km\\h")  # Printing Max Speed
NewVehicle.seating_capacity()
print("Fare of Vehicle:",NewVehicle.find_fare(),"PKR")      # Prints Vehicle fare

NewVehicle2 = Vehicle()      # Create instance of vehicle
print("Max Speed:",NewVehicle2.getMax_Speed(), "km\\h")  # Printing Max Speed
NewVehicle2.seating_capacity()
print("Fare of Vehicle:",NewVehicle2.find_fare(),"PKR")      # Prints Vehicle fare
