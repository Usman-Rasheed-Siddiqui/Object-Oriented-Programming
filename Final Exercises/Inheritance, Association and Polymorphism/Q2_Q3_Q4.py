
class Publication:
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

class Book(Publication, Sales):
    def __init__(self):
        self.page_count = 0
        self.get_data()

    def get_data(self):
        Publication.get_data(self)
        Sales.get_data(self)
        self.page_count = int(input("Enter the page count of book: "))

    def put_data(self):
        Publication.put_data(self)
        Sales.put_data(self)
        print(f"Page count: {self.page_count} pages")

class Tape(Publication):
    def __init__(self):
        self.playing_time = 0
        self.get_data()

    def get_data(self):
        super().get_data()
        self.playing_time = float(input("Enter the playing time of book: "))

    def put_data(self):
        super().put_data()
        print(f"Playing time: {str(self.playing_time)} minutes")

class disk_type(Publication):
    def __init__(self):
        self.disk_type = None
        self.get_data()

    def get_data(self):
        Publication.get_data(self)
        types = {"c": "CD", "d": "DVD"}
        user = input("Enter the disk type: ").lower()
        for type in types.keys():
            if user == type:
                self.disk_type = types[type]

    def put_data(self):
        Publication.put_data(self)
        print("Disk type: " + self.disk_type)

C1 = disk_type()
C1.put_data()