
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def add_time(self, other):
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds
        self.adjust_seconds()


    def subtract_time(self, other):
        if self.hours < other.hours:
            self.hours, other.hours = other.hours, self.hours
            self.minutes, other.minutes = other.minutes, self.minutes
            self.seconds, other.seconds = other.seconds, self.seconds

        if self.seconds < other.seconds:
            self.minutes -= 1
            self.seconds += 60

        self.seconds -= other.seconds

        if self.minutes < other.minutes:
            self.hours -= 1
            self.minutes += 60

        self.minutes -= other.minutes

        self.hours -= other.hours

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

    def __mul__(self, num):
        if self.hours > 0:
            new_hours = int(self.hours * num)
            return Time(new_hours, self.minutes, self.seconds)

        elif self.minutes > 0:
            new_minutes = int(self.minutes * num)
            return Time(self.hours,new_minutes, self.seconds)

        elif self.seconds > 0:
            new_seconds = int(self.seconds * num)
            return Time(self.hours,self.minutes, new_seconds)

T1 = Time(25, 3, 30)
T2 = Time(24, 6, 50)

Tnew = T1 * 2.0
Tnew.adjust_seconds()
print(Tnew)