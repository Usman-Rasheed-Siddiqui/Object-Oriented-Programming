
class Pencil:
    def __init__(self, c = "red"):
        self.color = c

    @property
    def COLOR(self):
        "This is property"
        return self.color

    @COLOR.setter
    def COLOR(self, value):
        self.color = value

    @COLOR.deleter
    def COLOR(self):
        del self.color

a = Pencil()
print(a.COLOR)
a.COLOR = "blue"
print(a.COLOR)
del a.COLOR
print(a.COLOR)      # Deleted attribute can't be called