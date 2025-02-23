
class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
        self.format_time()

    def __str__(self):
        return f"{f'{self.hours}' if self.hours >= 10 else f'0{self.hours}'}:{f'{self.minutes}' if self.minutes >= 10 else f'0{self.minutes}'}:{f'{self.seconds}' if self.seconds >= 10 else f'0{self.seconds}'}"

    def add_time(self, time):
        self.seconds += time.seconds
        self.minutes += time.minutes
        self.hours += time.hours
        self.format_time()
        return self

    def format_time(self):
        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
        while self.hours >= 24:
            self.hours -= 24

    def __sub__(self, other):

        total_self = self.hours *3600 + self.minutes *60 + self.seconds
        other_self = other.hours *3600 + other.minutes *60 + other.seconds

        if total_self < other_self:
            return Time(0 ,0 ,0)

        diff_seconds = total_self - other_self

        new_hours = 0
        new_minutes = 0
        new_seconds = 0

        while diff_seconds >= 3600:
            diff_seconds -= 3600
            new_hours += 1

        while diff_seconds >= 60:
            diff_seconds -= 60
            new_minutes += 1
        new_seconds = diff_seconds

        return Time(new_hours, new_minutes, new_seconds)

t1 = Time(2, 23, 60)
t2 = Time(1, 40, 50)
print(t1 - t2)
