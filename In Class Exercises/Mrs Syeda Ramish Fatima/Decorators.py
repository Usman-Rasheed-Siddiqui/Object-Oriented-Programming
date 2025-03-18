
# Define a decorator
def myDecorator(func):
    def Wrapper():
        print("Wrapper before execution")
        func()
        print("Wrapper after execution")

    return Wrapper

# Using a Decorator
@myDecorator
def myFunc():
    print("Decorated")

# Calling Function
myFunc()