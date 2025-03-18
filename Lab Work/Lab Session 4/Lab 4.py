
class Vehicle:
    def sh_vh(self):
        print("Inside vehicle class")

class Car(Vehicle):
    def sh_car(self):
        print("Inside car class")

v1 = Car()
v1.sh_vh()
v1.sh_car()
