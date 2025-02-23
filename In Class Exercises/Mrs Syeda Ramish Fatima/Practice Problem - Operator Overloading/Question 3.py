
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
        if self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        if self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
        if self.hours >= 24:
            self.hours -= 24

t1 = Time(12,24,60)
t2 = Time(23, 50, 70)

print(t2)
t1.add_time(t2)
print(t1)