import functools
import threading
import time

__all__ = ['event', 'timer']


class event:
    def __init__(self, owner, name: str = None):
        if name is None:
            self._name = hex(id(self))
        else:
            self._name = name

        self.__sender = owner
        self.__handlers = list()

    def __repr__(self):
        return f"event<{repr(self.__sender)}.{self._name}>"

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

    def __init__(self, name: str = None, interval: float = 0):
        timer.__id += 1
        self._id = timer.__id

        self.tick = event(self, 'tick')

        self._on = False
        self._interval = 0
        self.interval = interval
        self._thread = None

        if name is not None:
            self._name = name
        else:
            self._name = hex(id(self))

    @property
    def on(self):
        return self._on

    @on.setter
    def on(self, val: bool):
        if val:
            self.run()
        else:
            self.stop()

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, val: float):
        if val < 0:
            raise Exception("Can't set interval less than 0")
        self._interval = val

    def __repr__(self):
        return f"timer<{self._name}#{self._id}>"

    def run(self):
        self._on = True
        self._thread = threading.Thread(target=self.__tick)
        self._thread.start()

    def stop(self):
        self._on = False

    def __tick(self):
        while self.on:
            time.sleep(self._interval)
            self.tick.happen()


def handle(*events: event):
    def decorator(f):
        for e in events:
            e.hook(f)

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        return wrapper

    return decorator
