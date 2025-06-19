
class Fancy_Print:
    message = ""

    def set_message(self, message):
        Fancy_Print.message = message

    @staticmethod
    def decorator(func):
        def wrapper():
            print("*"*20)
            func()
            print("*"*20)
            print("*"*18)
            print("*"*16)
            print("*"*14)

        return wrapper

    @staticmethod
    @decorator
    def fancy_print():
        print(Fancy_Print.message.upper())

F1 = Fancy_Print()
F1.set_message("Hello")
F1.fancy_print()



