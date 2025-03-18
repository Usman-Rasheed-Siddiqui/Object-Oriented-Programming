from time import time

class Stopwatch:
    def __init__(self):
        self.reset()

    def start(self):
        self._start_time = time()  # Clock now running

    def stop(self):
        self._stop_time = time()  # Clock stopped

    def reset(self):
        self._start_time = self._stop_time = 0

    def elapsed(self):
        return self._stop_time - self._start_time

class DigitalStopwatch(Stopwatch):
    def __init__(self):
        super().__init__()
        print("Initializing digital stopwatch")

    def digital_time(self):
        seconds = round(self.elapsed())
        hours = seconds // 3600  # Compute total hours
        seconds %= 3600  # Update seconds remaining
        minutes = seconds // 60  # Compute minutes
        seconds %= 60  # Update seconds remaining
        return f'{hours:02}:{minutes:02}:{seconds:02}'

# Client Code
d = DigitalStopwatch()
d.start()

for _ in range(1000000000):
    pass

d.stop()
print(d.elapsed())
print(d.digital_time())
