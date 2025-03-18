class BankAccount:

    def __init__(self):
        self.name = None

    def main_menu(self):
        print("1. Check Your Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit")

    def exit_program(self):
        print("Thank you for using our bank")
        exit()

    def creating_file_of_names(self):
        # Opening the records of people to check if account exists
        with open("Names.txt","r") as names:    # Opening Records of People
            self.account_name = []
            for line in names:
                line = line.strip().split(',')
                line[1] = float(line[1])
                self.account_name.append(line)

        return self.account_name

    def set_account_name(self):
        '''Entering account name'''
        if not self.name:   # Only ask for name if it's not present
            self.name = input("Enter your name to access your account: ").upper()

    def get_account_name(self):
        '''Fetching account name'''
        if self.name is None:
            self.set_account_name()     # Ensure name is set if it hasn't been
        return self.name

    def new_account(self):
        '''In order to create a new account'''

        # For headings to be Bold And Italic
        self.bold_italic = '\033[1m\033[3m'
        self.reset = '\033[0m'

        import random
        new_name = input("Enter your name for your new account: ").upper()
        self.password = random.randint(1000, 9999)
        print(f"\nYour password is {self.bold_italic}{self.password}{self.reset}")

        with open("Names.txt", "a") as new_name_file:
            new_name_file.write(f"{new_name},0.0,{self.password}")
            new_name_file.write("\n")
        print("Your account was successfully created")
        return

    def check_password(self):
        '''To check for password'''
        self.accountant_info = self.get_accountant_info()
        attempt = 0

        while attempt<3:
            self.password = int(input("Enter your password: "))     # Enter your password
            if int(self.accountant_info[2]) == self.password:
                print(f"\nYour password is correct...")
                return self.main_menu()     # If the password is correct, it returns to main menu
            else:
                attempt += 1
                print(f"Password is incorrect, You have {3-attempt} attempt(s) left")

        print("You have exceeded the maximum amount of password. Access Denied")
        exit()

    def get_accountant_info(self):
        '''To get a specific accountant information'''
        self.accountants = self.creating_file_of_names()
        for i in range(len(self.accountants)):
            if self.accountants[i][0] == self.name:
                return self.accountants[i]


    def account_holder(self):
        '''In order to search for an existing account'''
        self.name = self.get_account_name()   # Asking UserName
        self.account_name = self.creating_file_of_names()

        # For headings to be Bold And Italic
        self.bold_italic = '\033[1m\033[3m'
        self.reset = '\033[0m'

        # Check if the account exists
        found = False
        for account in self.account_name:
            if account[0] == self.name:     # Matching Name with names in list
                print(f"Welcome {self.bold_italic}{self.name}{self.reset}")
                found = True

        if not found:   # If name not found
            print("We did not find your account")
            ask = input("Do you want to create an account? (Y/N): ")    # Ask to create a new account
            if ask.upper() == "Y":
                self.new_account()
            else:
                print("Thank you!")

# Methods:
    def balance(self):
        '''In order to show the account balance'''
        self.name = self.get_account_name()
        self.account_names = self.creating_file_of_names()
        self.accountant_info = self.get_accountant_info()
        self.current_balance = self.accountant_info[1]
        self.balance_length = len(str(self.current_balance))

        # For headings to be Bold And Italic
        self.bold_italic = '\033[1m\033[3m'
        self.reset = '\033[0m'

        # Adjusting Name row dynamically
        col_length_balance = max(len("Balance"), self.balance_length)
        col_length_name = max(len("Account Name"), len(self.name))

        # Adjusting the header column width dynamically
        header = '| '
        header += f"{self.bold_italic}{'Account Name':{col_length_name}}{self.reset} | {self.bold_italic}{'Balance':{col_length_balance}}{self.reset} |"
        print(header.strip())

        # Adjusting Name row dynamically
        row = '| '
        row += f"{self.name:{col_length_name}} | {self.current_balance:{col_length_balance}} |"
        print(row.strip())

    def deposit_amount(self):
        '''In order to deposit money to the account'''
        deposit_amount = float(input("How much amount you want to deposit: "))
        self.name = self.get_account_name()

        with open("Names.txt", "r") as amount_file:
            info = amount_file.readlines()

        # Modify account balance
        for i, line in enumerate(info):
            account_info = line.strip().split(',')
            if account_info[0] == self.name:
                # Update balance
                account_info[1] = str(float(account_info[1]) + deposit_amount)   # Add the deposited amount
                info[i] = ','.join(account_info) + '\n' # Recreate the line with updated balance
                break

        # Write the info back to the file
        with open("Names.txt", "w") as amount_file:
            amount_file.writelines(info)

        print(f"\nDeposit successful! New balance for {self.name} is {account_info[1]}")

    def withdraw_amount(self):
        '''In order to deposit money to the account'''
        self.name = self.get_account_name()

        while True:
            withdraw_amount = float(input("How much amount you want to withdraw: "))

            if withdraw_amount > float(self.accountant_info[1]):
                print("You don't have enough money in your account. Please enter an appropriate amount.")

            else:
                with open("Names.txt", "r") as amount_file:
                    info = amount_file.readlines()

                # Modify account balance
                for i, line in enumerate(info):
                    account_info = line.strip().split(',')
                    if account_info[0] == self.name:
                        # Update balance
                        account_info[1] = str(float(account_info[1]) - withdraw_amount)  # Add the deposited amount
                        info[i] = ','.join(account_info) + '\n'  # Recreate the line with updated balance
                        break
                break

        # Write the info back to the file
        with open("Names.txt", "w") as amount_file:
            amount_file.writelines(info)

        print(f"Withdraw successful! New balance for {self.name} is {account_info[1]}")


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