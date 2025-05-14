
def smart_division():
    try:
        dividend = float(input("Enter dividend: "))
        divisor = float(input("Enter divisor: "))
        if divisor == 0:
            raise ZeroDivisionError

    except ZeroDivisionError:
        print("Error: You can't divide by zero.")

    except ValueError:
        print("Error: Inappropriate input. Only numbers allowed.")

    else:
        answer = dividend / divisor
        answer = round(answer, 3)
        print(f"Answer: {answer}")

smart_division()