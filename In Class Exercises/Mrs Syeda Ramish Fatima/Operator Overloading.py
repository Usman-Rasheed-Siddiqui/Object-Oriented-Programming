class Overloading:
    def __init__(self,value):
        self.value = value

    def __add__(self,add):
        return self.value + add.value

    def __sub__(self,sub):
        return self.value - sub.value

    def __mul__(self,mul):
        return self.value * mul.value

    def __truediv__(self, truediv):
        return self.value / truediv.value

    def __floordiv__(self, floordiv):
        return self.value // floordiv.value

    def __mod__(self, mod):
        return self.value % mod.value

    def __pow__(self, pow):
        return self.value ** pow.value

    def __lt__(self, lt):
        return self.value < lt.value

    def __gt__(self, gt):
        return self.value > gt.value

    def __le__(self, le):
        return self.value <= le.value

    def __ge__(self, ge):
        return self.value >= ge.value

    def __eq__(self, eq):
        return self.value == eq.value

    def __ne__(self, ne):
        return self.value != ne.value

    def __iadd__(self, iadd):
        self.value += iadd.value
        return self

    def __isub__(self, isub):
        self.value -= isub.value
        return self

    def __imul__(self, imul):
        self.value *= imul.value
        return self

    def __itruediv__(self, ifloordiv):
        self.value /= ifloordiv.value
        return self

    def __ifloordiv__(self, ifloordiv):
        self.value //= ifloordiv.value
        return self

    def __imod__(self, imod):
        self.value %= imod.value
        return self

    def __ipow__(self, ipow):
        self.value **= ipow.value
        return self

    def __neg__(self):
        return -self.value

    def __pos__(self):
        return +self.value

    def __invert__(self):
        return ~self.value

    def __abs__(self):
        return abs(self.value)

    def __str__(self):
        return str(self.value)

OL1 = Overloading(10)
OL2 = Overloading(5)

print("Add: ",OL1 + OL2)
print("Sub: ",OL1 - OL2)
print("Mul: ",OL1 * OL2)
print("TrueDiv: ",OL1 / OL2)
print("FloorDiv: ",OL1 // OL2)
print("Mod: ",OL1 % OL2)
print("Pow: ",OL1 ** OL2)
OL1 += OL2
print("iAdd: ",OL1)
OL1 -= OL2
print("iSub: ",OL1)
OL1 *= OL2
print("iMul: ",OL1)
OL1 /= OL2
print("iTrueDiv: ",OL1)
OL1 //= OL2
print("iFloorDiv: ",OL1)
OL1 %= OL2
print("iMod: ",OL1)
OL1 **= OL2
print("iPow: ",OL1)
print("Neg: ", -OL2)
print("Pos: ", +OL2)
print("Invert: ", ~OL2)
print("Abs: ",abs(OL1))
