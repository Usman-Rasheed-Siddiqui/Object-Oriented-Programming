
from abc import ABC, abstractmethod

class Pencil(ABC):
    def __init__(self, color):
        self.color = color

    @property
    @abstractmethod
    def COLOR(self):
        '''This is a property'''
        return self.color

    @COLOR.setter
    def COLOR(self, value):
        '''This is a setter'''
        self.color = value

    @COLOR.deleter
    def COLOR(self):
        '''This is a deleter'''
        del self.color

class Child(Pencil):
    COLOR = 'yellow'

a = Child(1)
print(a.COLOR)
a.COLOR = 'red'
print(a.COLOR)
