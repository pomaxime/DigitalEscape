import time
from .item import Item


class Time(Item):
    def __init__(self, duration):
        self.duration = duration
        self.start_time = None
        self.end_time = None
        self.running = False

    def start(self):
        self.start_time = time.time()
        self.end_time = None
        self.running = True

    def stop(self):
        self.end_time = time.time()
        self.running = False

    def elapsed(self):
        if self.start_time is None:
            return 0

        end_time = time.time() if self.running else self.end_time
        return end_time - self.start_time

    def remaining(self):
        return max(0, self.duration - self.elapsed())
