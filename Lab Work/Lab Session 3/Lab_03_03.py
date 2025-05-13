from datetime import datetime

class Person:
    def __init__(self, name, birth_year: int):
        self.name = name
        self.birth_year = birth_year

    @classmethod
    def age_calculator(cls, person_instance):
        if not isinstance(person_instance, Person):
            print("Invalid instance. Please provide a Person instance.")

        current_year = datetime.now().year
        cls.age = current_year - person_instance.birth_year

    @staticmethod
    def check_age():
        if Person.age > 18:
            return True
        else:
            return False

P1 = Person("John", 1999)
P1.age_calculator(P1)
print(P1.check_age())
