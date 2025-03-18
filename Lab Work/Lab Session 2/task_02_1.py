
class BankAccount:
    def __init__(self):
        self.name = None

    def main_menu(self):
        print("1. Check Your Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit")

    def exit_program(self):
        print("Thank You for using our bank")
        exit()

    def set_account_name(self):
        if not self.name:
            self.name = input("Enter your name to access your account: ").upper()

    def get_account_name(self):
        if self.name is None:
            self.set_account_name()

        return self.name

    def creating_file_of_names(self):
        with open("Names.txt","r") as names:
            self.account_names = []
            for line in names:
                line = line.strip().split(",")
                line[1] = float(line[1])
                self.account_names.append(line)

        return self.account_names

    def get_account_info(self):
        self.accountants = self.creating_file_of_names()
        for i in range(len(self.accountants)):
            if self.accountants[i][0] == self.name:
                return self.accountants[i]

    def new_account(self):

        import random
        self.new_name = input("Enter your name for your account: ").upper()
        self.password = random.randint(1000,9999)
        print(f'Your password is {self.password}')

        with open("Names.txt", "a") as new_name_file:
            new_name_file.write(f"{self.new_name},0.0,{self.password}")
            new_name_file.write('\n')

        print("Your account has been created successfully")
        return

    def check_password(self):
        self.accountant_info = self.get_account_info()
        attempts =0

        while attempts < 3:
            self.password = int(input("Enter your password: "))
            if  int(self.accountant_info[2]) == self.password:
                print("Your password is correct.....")
                return self.main_menu()

            else:
                attempts += 1
                print(f"You have only {3-attempts} attempt(s) left")

        print("Your password limit has exceeded. Access Denied")
        exit()

    def account_holder(self):
        self.name = self.get_account_name()
        self.accounts_name = self.creating_file_of_names()

        found = False

        for account in self.accounts_name:
            if account[0] == self.name:
               print(f"Welcome {account[0]}")
               found = True

        if not found:
            print("We did not find your account...")
            exit()


    def balance(self):
        self.name = self.get_account_name()
        self.account_names = self.creating_file_of_names()
        self.accountant_info = self.get_account_info()
        self.current_balance = self.accountant_info[1]
        self.balance_length = len(str(self.current_balance))

        col_length_balance = max(len("Balance"), self.balance_length)
        col_length_name = max(len("Account Name"), len(self.name))


        header = '| '
        header += f"{'Account Name':{col_length_name}} | {'Balance':{col_length_balance}} |"
        print(header.strip())

        row = '| '
        row += f"{self.name:{col_length_name}} | {self.current_balance:{col_length_balance}} |"
        print(row.strip())

    def deposit_amount(self):
        self.depositing_amount = float(input("How much amount you want to deposit: "))
        self.name = self.get_account_name()

        if self.depositing_amount <= 0:
            print("Invalid Input")

        else:
            with open("Names.txt", "r") as amount_file:
                info = amount_file.readlines()

            for i,l2ine in enumerate(info):
                account_info = line.strip().split(',')
                if account_info[0] == self.name:
                    account_info[1] =  str(float(account_info[1]) + self.depositing_amount)
                    info[i] = ','.join(account_info) + '\n'
                    break

            with open("Names.txt", "w") as amount_file:
                amount_file.writelines(info)

            print(f"\nDeposit successful! New balance for {self.name} is {account_info[1]}")

    def withdraw_amount(self):
        self.withdrawing_amount = float(input("How much amount you want to withdraw: "))
        self.name = self.get_account_name()

        if self.withdrawing_amount > float(self.accountant_info[1]):
            print("You don't have enough money in your account. Please enter an appropriate amount.")

        else:
            with open("Names.txt", "r") as amount_file:
                info = amount_file.readlines()

            for i, line in enumerate(info):
                account_info = line.strip().split(',')
                if account_info[0] == self.name:
                    account_info[1] = str(float(account_info[1]) - self.withdrawing_amount)
                    info[i] = ','.join(account_info) + '\n'
                    break

            with open("Names.txt", "w") as amount_file:
                amount_file.writelines(info)

            print(f"\nWithdraw successful! New balance for {self.name} is {account_info[1]}")

Bank = BankAccount()

def main():
    print("------------")
    print("Welcome User")
    print("------------")
    print("1. Enter Existing Account")
    print("2. Create New Account")

    choice = input("Enter your choice: ")

    if choice == '1':
        # Entering with name:
        Bank.account_holder()
        Bank.check_password()
        while True:
            choice2 = input("Enter your choice: ")
            print()

            if choice2 == '1':
                Bank.balance()
            elif choice2 == '2':
                Bank.deposit_amount()
            elif choice2 == '3':
                Bank.withdraw_amount()
            elif choice2 == '4':
                Bank.exit_program()
            else:
                print("Please enter a valid choice")
            Bank.main_menu()

    elif choice == '2':
        Bank.new_account()
        return main()

    else:
        print("Please enter a valid choice")

main()
