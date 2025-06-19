
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.adjust_seconds()

    def add_time(self, other):
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds
        self.adjust_seconds()

    def adjust_seconds(self):
        while self.seconds > 60:
            self.minutes += 1
            self.seconds -= 60

        self.adjust_minutes()

    def adjust_minutes(self):
        while self.minutes > 60:
            self.hours += 1
            self.minutes -= 60

        self.adjust_hours()

    def adjust_hours(self):
        while self.hours > 24:
            self.hours -= 24

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"



T1 = Time(25, 61, 30)
print(T1)

T2 = Time(2, 60, 40)
print(T2)

T1.add_time(T2)
print(T1)