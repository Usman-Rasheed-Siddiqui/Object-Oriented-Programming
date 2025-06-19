
class Vehicle:
    def __init__(self, engine):
        self.__no_of_wheels = 0
        self.__color = ""
        self.__model_no = ""
        self.engine = engine

    def set_no_of_wheels(self, no_of_wheels):
        self.__no_of_wheels = no_of_wheels

    def set_color(self, color):
        self.__color = color

    def set_model_no(self, model_no):
        self.__model_no = model_no

    def get_no_of_wheels(self):
        return self.__no_of_wheels

    def get_color(self):
        return self.__color

    def get_model_no(self):
        return self.__model_no

    def display(self):
        print(self.__no_of_wheels, self.__color, self.__model_no)

class Engine:
    def __init__(self):
        self.__engine_no = 0
        self.__date_of_manufacture = ""

    def set_engine_no(self, engine_no):
        self.__engine_no = engine_no

    def set_date_of_manufacture(self, date_of_manufacture):
        self.__date_of_manufacture = date_of_manufacture

    def get_engine_no(self):
        return self.__engine_no

    def get_date_of_manufacture(self):
        return self.__date_of_manufacture

    def display_engine(self):
        print(self.__engine_no, self.__date_of_manufacture)

V1 = Vehicle(Engine())
V1.set_no_of_wheels(1)
V1.set_color("red")
V1.set_model_no(2)
V1.display()
print()
V1.engine.set_engine_no(3)
V1.engine.set_date_of_manufacture("2/2/25")
V1.engine.display_engine()