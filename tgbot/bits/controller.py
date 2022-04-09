import threading
import time

__all__ = ['event', 'timer']


class event:
    def __init__(self, owner, name=None):
        if name is None:
            self.name = hex(id(self))
        else:
            self.name = name

        self.owner = owner
        self.handlers = list()

    def __repr__(self):
        return f"event<{repr(self.owner)}.{self.name}>"

    def hock(self, handler):
        self.handlers.append(handler)

    def happen(self, message=None):
        for h in self.handlers:
            h(message)


class timer:
    __id__ = 0

    def __init__(self, name=None, interval=0):
        self.on = False
        self.interval = interval
        self.tick = event(self, 'tick')
        self.thread = None
        timer.__id__ += 1
        self.id = timer.__id__
        if name is not None:
            self.name = name
        else:
            self.name = hex(id(self))

    def __repr__(self):
        return f"timer<{self.name}#{self.id}>"

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
