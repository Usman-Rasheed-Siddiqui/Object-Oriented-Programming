class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __str__(self):
        return f"<{self.x} , {self.y}>"

P1 = Point(1, 2)
print(-P1)
