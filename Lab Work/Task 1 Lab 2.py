
class BankAccount:
    accounts = {}
    def __init__(self, name=None,password=None, balance=0):
        self.name = name
        self.password = password
        self.balance = balance
        if self.name:
            self.check_password()

    def create_account(self):
        self.name = input("Enter your name: ")
        self.password = input("Enter your password: ")
        self.balance = int(input("Enter your balance: "))
        BankAccount.accounts[self.name] = [self.password, self.balance]
        print("Your account has been created")

    def check_password(self):
        if self.name not in BankAccount.accounts:
            print("Please create an account first")
            exit()
        elif self.password == BankAccount.accounts[self.name][0]:
            print("Your password is correct.")
        else:
            print("Your password is incorrect.")
            exit()

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        return self.balance

# Create an instance and call create_account before any actions
B1 = BankAccount()
B1.create_account()

# After creating an account, now you can use other functionalities
B1.deposit(500)
B1.withdraw(200)
print("Final balance:", B1.check_balance())