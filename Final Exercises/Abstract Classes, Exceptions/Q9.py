
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def set_x(self):
        try:
            self.x = float(input("Enter x coordinate: "))
            if not isinstance(self.x, (int, float)):
                raise ValueError

        except ValueError:
            print("Error: x must be an integer or float.")

        except KeyboardInterrupt:
            print("You interrupted.")

    def set_y(self):
        try:
            self.y = float(input("Enter y coordinate: "))
            if not isinstance(self.y, (int, float)):
                raise ValueError

        except ValueError:
            print("Error: y must be an integer or float.")

        except KeyboardInterrupt:
            print("You interrupted.")

    def display_point(self):
        return self.x, self.y


P1 = Point()

try:
    P1.set_x()
    P1.set_y()
    print(P1.display_point())

except AttributeError as e:
    print("Error:", e)
