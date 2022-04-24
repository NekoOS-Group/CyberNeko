import threading
import time

__all__ = ['event', 'timer']


class event:
    def __init__(self, owner, name=None):
        if name is None:
            self.name = hex(id(self))
        else:
            self.name = name

        self.__sender = owner
        self.__handlers = list()

    def __repr__(self):
        return f"event<{repr(self.__sender)}.{self.name}>"

    def hook(self, handler):
        self.__handlers.append(handler)

    def happen(self, message=None):
        for h in self.__handlers:
            if message is None:
                h(self.__sender)
            else:
                h(self.__sender, message)


class timer:
    __id = 0

    def __init__(self, name=None, interval=0):
        self.on = False
        self.interval = interval
        self.tick = event(self, 'tick')
        self.__thread = None
        timer.__id += 1
        self.id = timer.__id
        if name is not None:
            self.name = name
        else:
            self.name = hex(id(self))

    def __repr__(self):
        return f"timer<{self.name}#{self.id}>"

    def run(self):
        self.on = True
        self.__thread = threading.Thread(target=self.__tick)
        self.__thread.start()

    def stop(self):
        self.on = False

    def __tick(self):
        while self.on:
            time.sleep(self.interval)
            self.tick.happen()
