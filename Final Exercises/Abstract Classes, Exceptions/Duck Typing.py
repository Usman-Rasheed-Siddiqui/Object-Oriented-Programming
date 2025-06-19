
class Airplaine:
    def fly(self):
        print("fly with fuel")

class Duck:
    def fly(self):
        print("fly with wings")

    def swim(self):
        print("swim in ponds")

class Fish:
    def swim(self):
        print("swim in sea")

def move(thing):
    thing.fly()


a = Airplaine()
d = Duck()
f = Fish()

move(a)
move(d)
