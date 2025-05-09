
# Custom exception classes for handling specific exceptions in the Library System
class UserNotFoundError(Exception):
    def __init__(self):
        self.message = 'User not found'
        super().__init__(self.message)

    def __str__(self):
        return self.message

class PasswordNotMatchError(Exception):
    def __init__(self):
        self.message = 'Password does not match'
        super().__init__(self.message)

    def __str__(self):
        return self.message

class AlreadyExistError(Exception):
    pass    # Raised when a username or password already exist

class BookNotAvailableError(Exception):
    pass    # Raised when a book is not available for borrowing

class BookNotFoundError(Exception):
    pass    # Raised when a book doesn't exist in the library

class BalanceError(Exception):
    pass    # Raised for balance-related issues

class PasswordRangeError(Exception):
    pass    # Raised when password doesn't meet length requirements

class BookNotBorrowedError(Exception):
    pass    # Raised when trying to return a book that wasn't borrowed

class Library:
    def __init__(self, name="", password="", book=""):
        # Initialize library with default values
        self.name = name            # Current user's name
        self.password = password    # Current user's password
        self.book = book            # Current book being processed
        self.cost = 0               # Cost of current book
        self.balance = 0            # Current user's balance
        self.main_menu()            # Start with main menu

    # Predefined user accounts with passwords, borrowed books, and balances
    _accounts = {
        "Alice": {
            "password": "alice123",
            "borrowed": [],
            "balance": 500,
        },
        "Ahmed": {
            "password": "Ahmed#886",
            "borrowed": [],
            "balance": 300,
        },
        "Charlie": {
            "password": "charliePwd!",
            "borrowed": [],
            "balance": 750,
        },
        "Ayesha": {
            "password": "AyeshaSecret",
            "borrowed": [],
            "balance": 1000,
        },
        "Ali": {
            "password": "Ali_e",
            "borrowed": [],
            "balance": 200,
        }
    }

    # Predefined books with their details
    _books = {
        "101": {"title": "Dr. Jekyll and Mr. Hyde", "cost": 100, "available": True},
        "102": {"title": "To Kill a Mockingbird", "cost": 250, "available": True},
        "103": {"title": "1984", "cost": 180, "available": True},
        "104": {"title": "The Great Gatsby", "cost": 220, "available": False},
        "105": {"title": "Pride and Prejudice", "cost": 150, "available": True},
        "106": {"title": "The Hobbit", "cost": 300, "available": True},
        "107": {"title": "Harry Potter and the Sorcerer's Stone", "cost": 350, "available": False},
        "108": {"title": "The Catcher in the Rye", "cost": 190, "available": True},
        "109": {"title": "Brave New World", "cost": 210, "available": True},
        "110": {"title": "The Alchemist", "cost": 170, "available": True}
    }

    @classmethod
    def accounts(cls):
        """Class method to access accounts dictionary"""
        return cls._accounts

    @classmethod
    def books(cls):
        "Class method to access books dictionary"
        return cls._books

    def quit_choice(self, choice):
        """Check if user wants to quit (entered 'q' or 'Q')"""
        if choice == "q" or choice == "Q":
            return True
        return False

    def login(self):
        """Handle user login process"""
        print()
        print("=" * 30)
        print("Login")
        print("=" * 30)
        print()
        print("Enter q/Q at any time to quit to main menu.")

        # Get username and password
        self.name = input("Enter your name: ").strip()
        if self.quit_choice(self.name):
            return self.main_menu()
        self.password = input("Enter your password: ").strip()
        if self.quit_choice(self.password):
            return self.main_menu()

        # Validate credentials
        while True:
            try:
                user_found = False
                for account, details in Library.accounts().items():
                    if account.lower() == self.name.lower():
                        user_found = True
                        if details["password"] == self.password:
                            self.name = account
                            print(f"Password matched\nWelcome Mr./Mrs. {self.name.upper()}")
                            return True     # Successful login
                        else:
                            raise PasswordNotMatchError

                if not user_found:
                    raise UserNotFoundError()

            except UserNotFoundError as e:
                print("Error:",e)
                break
            except PasswordNotMatchError as e:
                print("Error:",e)
                break

    def make_account(self):
        """Handle new account creation"""
        print()
        print("="*30)
        print("Sign Up")
        print("="*30)
        print()
        print("Enter q/Q at any time to quit to main menu.")

        # Get and validate username
        while True:
            try:
                self.name = input("Enter your name: ").strip()
                if self.quit_choice(self.name):
                    return self.main_menu()
                if not self.name.isalpha() or not self.name:
                    raise TypeError("Enter Correct Name (letter only, no spaces allowed)")
                if self.name in self.accounts():
                    raise AlreadyExistError
                break
            except TypeError as e:
                print("Error:",e)
            except AlreadyExistError:
                print("Username already exists")

        # Get and validate password
        while True:
            try:
                self.password = input("Enter your password (8+ characters): ").strip()
                if self.quit_choice(self.password):
                    return self.main_menu()
                if not self.password:
                    raise ValueError("This field is required")
                if len(self.password) < 8:
                    raise PasswordRangeError("Password must be at least 8 characters long")
                for account in self.accounts().values():
                    if account["password"] == self.password:
                        raise AlreadyExistError
                break
            except ValueError as e:
                print("Error:",e)
            except AlreadyExistError:
                print("Password already exists")
            except PasswordRangeError as e:
                print("Error:",e)

        # Get and validate initial balance
        while True:
            try:
                self.balance = input("Enter your balance: ")
                if self.quit_choice(self.balance):
                    return self.main_menu()
                if not self.balance.isdigit():
                    raise TypeError
                self.balance = int(self.balance)
                if self.balance <= 100:
                    raise ValueError("Balance must be greater than 100")
                if self.balance > 5000:
                    raise OverflowError("Balance is exceeding limit. Your total balance should be at most 5000.")
                break
            except TypeError:
                print("Invalid balance")
            except ValueError as e:
                print("Error:",e)
            except OverflowError as e:
                print("Error:",e)

        # Create new account with validated details
        account ={
        "password": self.password,
        "borrowed": [],
        "balance": self.balance,
        }

        Library._accounts[self.name] = account

        print("Account created successfully. Please login to access your account.")
        return self.main_menu()


    def save_book_id(self, id):
        """Update user account after borrowing a book"""
        for account, details in self.accounts().items():
            if account == self.name:
                if details["balance"] < self.cost:
                    print("You have insufficient balance")
                    self.user_menu()
                    break
                details["borrowed"].append(id)      # Add book to borrowed list
                details["balance"] -= self.cost     # Deduct cost from balance
                print(f"You succesfully borrowed this book. Your account balance is now {details['balance']}")
                break

    def borrow_book(self):
        """Handle book borrowing process"""
        print()
        print("=" * 30)
        print("Borrowing Book")
        print("=" * 30)
        print()
        print("Enter q/Q at any time to quit to user menu.")

        # Taking input for book and validating the input
        try:
            self.book = input("Enter available book's id to borrow: ")
            if self.quit_choice(self.book):
                return self.user_menu()
            book_found = False

            if self.book not in Library.books():
                raise KeyError("Book ID does not exist")

            for account, details in Library.accounts().items():
                if account == self.name:
                    if self.book in details["borrowed"]:
                        raise AlreadyExistError

            for id, book in Library.books().items():
                if self.book == id:
                    book_found = True
                    if book["available"]:
                        self.cost = book["cost"]
                        self.save_book_id(self.book)
                    else:
                        raise BookNotAvailableError
            if not book_found:
                raise BookNotFoundError
        except BookNotAvailableError:
            print("This book is currently not available")
        except BookNotFoundError:
            print("Sorry! We don't have this book")
        except KeyError as e:
            print("Error:",e)
        except AlreadyExistError:
            print("Book is already borrowed by you. Please choose one you did not borrow.")

        return self.user_menu()

    def return_book(self):
        print()
        print("=" * 30)
        print("Returning Book")
        print("=" * 30)
        print()
        print("Enter q/Q at any time to quit to user menu.")
        try:
            for account, details in Library.accounts().items():
                if account == self.name:
                    if not details["borrowed"]:
                        raise BookNotBorrowedError("No books borrowed")
                    id = input("Enter book ID: ")
                    if self.quit_choice(id):
                        return self.user_menu()
                    if not id.isdigit():
                        raise ValueError
                    for book_id in details["borrowed"]:
                        if book_id == id:
                            details["borrowed"].remove(id)
                            print("Book returned succesfully")
                            if id in Library.books():
                                Library.books()[id]["available"] = True  # Correct this
                            return self.user_menu()

        except ValueError:
            print("Invalid book ID")

        except BookNotBorrowedError as e:
            print("Error:",e)


    def update_balance(self):

        try:
            for account, details in Library.accounts().items():
                if account == self.name:
                    print("Enter q/Q at any time to quit to user menu.")
                    update_balance = input("Enter your new balance to be added: ")
                    if self.quit_choice(update_balance):
                        return self.user_menu()
                    if not update_balance.isdigit():
                        raise ValueError("Please enter a appropriate balance")
                    update_balance = int(update_balance)
                    if update_balance <= 0:
                        raise ValueError("Balance must be greater than 0")
                    if (details["balance"] + update_balance) > 5000:
                        raise OverflowError("Balance is exceeding limit. Your total balance should be at most 5000.")
                    details["balance"] += update_balance

                    if details["balance"] < 100:
                        raise BalanceError("Balance must be greater than 100")
            print("Balance updated successfully")
        except BalanceError as e:
            print("Error:",e)
        except ValueError as e:
            print("Error:",e)
        except OverflowError as e:
            print("Error:", e)

    def status(self):
        for account, details in Library.accounts().items():
            if account == self.name:
                print("\n","="*30)
                print(f"Borrowed Books ID: {details['borrowed'] if details['borrowed'] else 'No books borrowed'}")
                print(f"Balance: {details['balance']}")
                print("=" * 30)
                print()

    def view_all_books_available(self):
        print("\n","="*30)
        print("Available Books")
        print("="*30)
        for id, book in Library.books().items():
                if book.get("available"):
                    print("ID:", id, end="  |  ")
                    print(f"Title: {book['title']}  |  Cost: {book['cost']}  |  Availability: Available")
        print("=" * 30)
        print()

    def choice_main(self):
        while True:
            try:
                choice = input("\nEnter your choice here: ")
                if choice == "1":
                    if self.login():
                        self.user_menu()
                    else:
                        self.main_menu()
                elif choice == "2":
                    self.make_account()
                elif choice == "3":
                    print("Thank you for using our application")
                    exit()
                if not choice.isdigit():
                    raise TypeError
                if int(choice) < 1 or int(choice) > 3:
                    raise ValueError
            except TypeError:
                print("Error: You did not enter a number. Please enter a number between 1 and 3")
            except ValueError:
                print("Please enter a number between 1 and 3")

    def choice_user(self):
        while True:
            try:
                print("Press q/Q to quit to main menu. (You have to then login again)")
                choice = input("\nEnter your choice here: ")
                if self.quit_choice(choice):
                    return self.main_menu()
                if choice == "1":
                    self.borrow_book()
                elif choice == "2":
                    self.return_book()
                elif choice == "3":
                    self.update_balance()
                elif choice == "4":
                    self.status()
                elif choice == "5":
                    self.view_all_books_available()
                elif choice == "6":
                    self.main_menu()
                if not choice.isdigit():
                    raise TypeError
                if int(choice) < 1 or int(choice) > 6:
                    raise ValueError

            except TypeError:
                print("Error: You did not enter a number. Please enter a number between 1 and 6")
            except ValueError:
                print("Please enter a number between 1 and 6")


    def main_menu_interface(self):
        print("Please choose from the following options:")
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit Program")
        print("=" * 30)
        print()

    def main_menu(self):
        print("="*30)
        print("Welcome to our Library")
        print("="*30)
        self.main_menu_interface()
        self.choice_main()

    def user_menu_interface(self):
        print("=" * 30)
        print(f"Mr./ Mrs {self.name.upper()}'s Dashboard")
        print("=" * 30)
        print("Please choose from the following options:")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. Update Balance")
        print("4. Check Status")
        print("5. View All Books Available")
        print("6. Exit to Main Menu")
        print("=" * 30)
        print()

    def user_menu(self):
        self.user_menu_interface()
        self.choice_user()

L1 = Library()