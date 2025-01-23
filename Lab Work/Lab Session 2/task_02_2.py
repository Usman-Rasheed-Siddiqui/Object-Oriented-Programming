
class Toll_Booth:
    def __init__(self):
        self.num_car = 0
        self.total_money = 0
        self.defaulters = 0

    def paying_car(self):
        self.total_money += 50
        self.num_car += 1

    def no_pay_car(self):
        self.num_car += 1
        self.defaulters += 1

    def get_num_car(self):
        return self.num_car

    def get_money_collected(self):
        return self.total_money

    def get_defaulter(self):
        return self.defaulters

    def display(self):
        print(f"No. of cars passed: {self.get_num_car()}")
        print(f"Total money collected: {self.get_money_collected()}")
        print(f"No. of defaulters: {self.get_defaulter()}")


tollbooth = Toll_Booth()

while True:
    print("1. Increase No. of paying cars")
    print("2. Increase No. of no paying cars")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        tollbooth.paying_car()
    if choice == "2":
        tollbooth.no_pay_car()
    if choice == "3":
        tollbooth.display()
    if choice == "4":
        break