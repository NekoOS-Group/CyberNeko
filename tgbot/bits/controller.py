import threading
import time


class event:
    def __init__(self):
        self.handlers = list()

    def hock(self, handler):
        self.handlers.append(handler)

    def happen(self, message=None):
        for h in self.handlers:
            h(message)


class timer:
    def __init__(self, interval=0):
        self.on = False
        self.interval = interval
        self.tick = event()
        self.thread = None

    def run(self):
        self.on = True
        self.thread = threading.Thread(target=self.__tick__)
        self.thread.start()

    def stop(self):
        self.on = False

    def __tick__(self):
        while self.on:
            time.sleep(self.interval)
            self.tick.happen()
