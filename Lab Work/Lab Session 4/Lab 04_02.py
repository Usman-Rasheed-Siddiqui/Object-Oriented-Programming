class Bank_Account:
    def __init__(self):
        self.account_no = int(input("Enter your account no.: "))

    def showAccountInfo(self):
        print(f"Account No.: {self.account_no}")

class Saving_Account(Bank_Account):
    def __init__(self):
        super().__init__()
        self.minimum_balance = int(input("Enter Minimum Balance: "))
        self.interest_rate = int(input("Enter Interest Rate: "))

    def showAccountInfo(self):
        super().showAccountInfo()
        print(f"Minimum Balance: {self.minimum_balance}")
        print(f"Interest Rate: {self.interest_rate}")


class Current_Account(Bank_Account):
    def __init__(self):
        super().__init__()
        self.withdrawl_limit = int(input("Enter Withdrawal Limit: "))

    def showAccountInfo(self):
        Bank_Account.showAccountInfo(self)
        print(f"Withdrawal Amount: {self.withdrawl_limit}")


sa1 = Saving_Account()
sa1.showAccountInfo()
sa2 = Current_Account()
sa2.showAccountInfo()