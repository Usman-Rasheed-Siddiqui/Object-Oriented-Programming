
class Exponential:
    def __init__(self):
        self.base = 1
        self.exponent = 1

    def set_base(self):
        self.base = int(input("Enter the base number: "))
        if self.base == 0:
            raise ValueError("Invalid values")

    def set_exponent(self):
        self.exponent = int(input("Enter the exponent number: "))
        if self.exponent == 0:
            raise ValueError("Invalid values")

    def __str__(self):
        return f"{self.base}^{self.exponent}"

    def __mul__(self, other):
        if self.base == other.base:
            self.exponent += other.exponent
            return self
        else:
            raise Exception("Cannot Multiply")

try:
    E1 = Exponential()
    E2 = Exponential()
    E1.set_base()
    E1.set_exponent()
    E2.set_base()
    E2.set_exponent()
    print(E1 * E2)

except ValueError as e:
    print("Error:",e)

except AttributeError as e:
    print("Error:",e)

except Exception as e:
    print("Error:",e)
