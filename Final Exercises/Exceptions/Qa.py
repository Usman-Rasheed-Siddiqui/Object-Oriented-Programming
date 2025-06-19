
class OutOfRangeError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def input_in_range(min_value, max_value):
    range_list = []
    for i in range(min_value, max_value + 1):
        range_list.append(i)

    try:
        num = int(input(f"Enter a number within {min_value} and {max_value}: "))
        if num in range_list:
            return num
        else:
            raise OutOfRangeError(f"The number {num} is out of range")
    except ValueError:
        print('\nPlease enter a number')

    except OutOfRangeError as e:
        print("Error:", e)

    except KeyboardInterrupt:
        print('\nYou terminated the program')

def create_list(n, min_value, max_value):
    range_list = []

    print(f"Enter {n} values")
    for i in range(n):
        while True:
            value = input_in_range(min_value, max_value)
            if value:
                range_list.append(value)
                break
    return range_list

print(create_list(5, 1, 10))


