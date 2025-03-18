
class Time:
    def __init__(self, h=0,m=0,s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def addTime(self, t):
        self.seconds += t.seconds
        if self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        self.minutes += t.minutes
        if self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
        self.hours += t.hours
        if self.hours >= 24:
            self.hours -= 24

t1 =Time()
print(t1)

t2 = Time(2,4,60)
print(t2)

t3 = Time(24,60,2)
print(t3)
