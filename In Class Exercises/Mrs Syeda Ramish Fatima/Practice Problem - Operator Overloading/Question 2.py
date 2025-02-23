
class Fraction:
    def __init__(self, n, d):
        if d == 0:
            print("Denominator cannot be zero. Setting value to 1")
            self.denominator = 1
        self.numerator = n
        self.denominator = d
        self.simplify()

    def setNumer(self, n):
        self.numerator = n
        self.simplify()

    def setDenom(self, d):
        if d == 0:
            print("Denominator cannot be zero. Setting value to 1")
            self.denominator = 1
        self.denominator = d
        self.simplify()

    def getNumer(self):
        return self.numerator

    def getDenom(self):
        return self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def HCF(self,a, b):
        '''Finding the Highest Common Factor'''
        while b:
            temp = a % b
            a = b
            b = temp
        return a

    def simplify(self):
        '''Simplifies the fraction using HCF'''
        hcf = self.HCF(self.numerator ,self.denominator)
        self.numerator //= hcf
        self.denominator //= hcf
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other):
        '''Overloads + operator to add two fractions'''
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator ,new_denominator)

    def __sub__(self, other):
        '''Overloads - operator to subtract two fractions'''
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator ,new_denominator)

    def __mul__(self, other):
        '''Overloads * operator to multiply two fractions'''
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator ,new_denominator)

    def __truediv__(self, other):
        '''Overloads / operator to divide two fractions'''
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator ,new_denominator)

    def __gt__(self, other):
        '''Overloads > operator to compare two fractions'''
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __lt__(self, other):
        '''Overloads < operator to compare two fractions'''
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __ge__(self, other):
        '''Overloads >= operator to compare two fractions'''
        return self.numerator * other.denominator >= other.numerator * self.denominator
    def __le__(self, other):
        '''Overloads <= operator to compare two fractions'''
        return self.numerator * other.denominator <= other.numerator * self.denominator

F1 = Fraction(6, 5)
F2 = Fraction(8, 9)

print(F1 + F2)
print(F1 - F2)
print(F1 < F2)
