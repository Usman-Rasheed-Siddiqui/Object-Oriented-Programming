
def input_list():
    int_list = []
    for i in range(1, 4):
        while True:
            try:
                num = int(input(f"Enter a num between 1, 100: "))
                if 1 <= num <= 100:
                    int_list.append(num)
                    break
                else:
                    raise Exception

            except ValueError:
                print("Error: Please enter an integer")

            except Exception:
                print("Error: Enter num between 1 and 100")

    return int_list

try:
    with open("my_list.txt", "a") as file:
        int_list = input_list()
        file.write(str(int_list) + "\n")

except FileNotFoundError:
    print("Error: Please enter a valid file")

else:
    with open("my_list.txt", "r") as file:
        print("The file now looks like this:")
        for line in file:
            print(line)

finally:
    print("File Updated Successfully")


