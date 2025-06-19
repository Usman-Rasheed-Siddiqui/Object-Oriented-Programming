
from collections.abc import Container

class OddContainer:
    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2:
            return False
        return True

num=OddContainer()
print(1 in num)
print(2 in num)
print(237813 in num)
print(isinstance(num,OddContainer))
print(issubclass(OddContainer,Container))