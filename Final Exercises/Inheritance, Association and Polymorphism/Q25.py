
class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

    def set_numerator(self):
        self.numerator = int(input("Please enter the numerator: "))

    def set_denominator(self):
        try:
            self.denominator = int(input("Please enter the denominator: "))
            if self.denominator == 0:
                self.denominator = 1
                raise ZeroDivisionError("Denominator cannot be zero. Setting denominator to 1")
        except ZeroDivisionError as e:
            print("Error:", e)

    def find_LCM(self, other):
        LCM = self.denominator * other.denominator
        self.numerator *= other.denominator
        other.numerator *= self.denominator

    def __add__(self, other):
        self.find_LCM(other)
        self.numerator += other.numerator

    def compute_GCD(self, num, denom):
        while denom != 0:
            num, denom = denom, num % denom
        return abs(num)

    def simplify(self):
        GCD  = self.compute_GCD(self.numerator, self.denominator)
        self.numerator //= GCD
        self.denominator //= GCD
        return self

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

F1 = Fraction()
F1.set_numerator()
F1.set_denominator()
F1.simplify()
print(F1)


