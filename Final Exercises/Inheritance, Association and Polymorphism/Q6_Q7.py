
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

D1 = Date(3)

print(D1)

