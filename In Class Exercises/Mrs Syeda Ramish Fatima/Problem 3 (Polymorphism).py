
class MyStr:
    def __init__(self, s=''):
        self.strg = s

    def __add__(self, anyObject):
        return self.strg + str(anyObject)

x = MyStr("Python")
print(x + "Programming")

