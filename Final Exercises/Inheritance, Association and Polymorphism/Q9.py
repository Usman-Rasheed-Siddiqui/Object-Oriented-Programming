
class Publication:

    count_books = 0
    count_tapes = 0
    books = []

    def __init__(self):
        self.title = ""
        self.price = 0.0
        self.get_data()

    def get_data(self):
        self.title = input("Enter the title of book: ")
        self.price = float(input("Enter the price of book: "))

    def put_data(self):
        print("Title: " + self.title)
        print("The price of book is: $", self.price)

    def get_books(self):
        print("Books: ")
        for i, book in enumerate(self.books, start=1):
            print(f"Book {i}: {book}")

class Sales:
    def __init__(self):
        self.get_data()

    def get_data(self):
        self.records = []
        for i in range(1, 4):
            record = float(input(f"Enter the price of sale for month {i}: "))
            self.records.append(record)

    def put_data(self):
        for num, record in enumerate(self.records, start=1):
            print(f"{num} month sale: ${record}")


class Date:
    def __init__(self, format):
        self.format = format
        self.month_name = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August",
                           "09": "September", 10: "October", 11: "November", 12: "December"}
        self.get_date()
        self.get_month()
        self.get_year()

    def get_date(self):
        self.date = int(input(f"Enter the date: "))
        if self.date < 10:
            self.date = "0"+str(self.date)

    def get_month(self):
        self.month = int(input(f"Enter the month: "))
        if self.month < 10:
            self.month = "0"+str(self.month)

    def get_year(self):
        self.year = int(input(f"Enter the year: "))
        if self.year < 10:
            self.year = "0"+str(self.year)

    def set_date(self):
        return self.date

    def set_month(self):
        return self.month

    def set_year(self):
        return self.year

    def __str__(self):
        if self.format == 1:
            return f"{self.date}-{self.month}-{self.year}"

        elif self.format == 2:
            return f"{self.month}/{self.date}/{self.year}"

        elif self.format == 3:
            return f"{self.month_name[self.month]} {self.date}, {self.year}"


class Book(Publication, Sales):

    def __init__(self):
        self.count_books += 1
        self.page_count = 0
        self.get_data()

    def get_data(self):
        Publication.get_data(self)
        Sales.get_data(self)
        self.page_count = int(input("Enter the page count of book: "))
        self.books["page_count"] = self.page_count

    def put_data(self):
        Publication.put_data(self)
        Sales.put_data(self)
        print(f"Page count: {self.page_count} pages")

    def print_books_count(self):
        print("Number of books: ", self.count_books)


class Tape(Publication):

    tapes = []

    def __init__(self):

        self.count_tapes += 1
        self.playing_time = 0
        self.format = None
        self.get_data()

    def get_data(self):
        super().get_data()
        self.playing_time = float(input("Enter the playing time of book: "))
        self.format = int(input("Enter the format for date (1,2 or 3): "))
        self.date = Date(self.format)

        tape = {}
        tape["title"] = self.title
        tape["price"] = self.price
        tape["playing_time"] = self.playing_time
        tape["date"] = self.date
        self.tapes.append(tape)

    def put_data(self):
        super().put_data()
        print("Date of Publication is:",self.date)
        print(f"Playing time: {str(self.playing_time)} minutes")

    def print_tapes(self):
        print("Number of tapes: ", len(self.tapes))
        for tape in self.tapes:
            for key, val in tape.items():
                print(f"{key}: {val}", end = " ")
            print()

T1 = Tape()
T2 = Tape()
T2.print_tapes()
