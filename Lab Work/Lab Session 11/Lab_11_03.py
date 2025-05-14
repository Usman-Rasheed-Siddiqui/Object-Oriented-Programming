
def factorial_calculator():
    try:
        factorial = int(input("Enter a number to calculate factorial: "))
        if factorial <= 0:
            raise Exception("Input cannot be zero or less than zero.")

        num = factorial
        for i in range(factorial-1, 0, -1):
            num *= i

    except ValueError:
        print("Error: Please enter an integer to calculate factorial.")

    except Exception as e:
        print("Error:",e)

    else:
        print(f"Answer: {factorial}! = {num}")

factorial_calculator()


