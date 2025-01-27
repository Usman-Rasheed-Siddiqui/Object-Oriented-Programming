
class Modifier:
    def __init__(self):
        self.value = 10

    def modified_value(self):
        self.value += 5
        print("Modified value is now:", self.value)

modify = Modifier()
modify.modified_value()
