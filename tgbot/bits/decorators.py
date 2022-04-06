from tgbot.bits.strings import decorating
import functools
import logging
import time


def bread(begin=None, end=None):
    def decorator(f):

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            message = None

            if begin is not None:
                message = begin(f, *args, **kwargs)

            ret = f(*args, **kwargs)

            if end is not None:
                if message is not None:
                    kwargs['message_by_begin'] = message
                if ret is not None:
                    kwargs['message_by_function'] = ret

                end(f, *args, **kwargs)

            return ret

        return wrapper

    return decorator


def log_enter(logger=None, logArgs=False):
    def log(f, *args, **kwargs):
        if logArgs:
            arg = "(" + ", ".join([repr(x) for x in args] + [f"{k}={v!r}" for k, v in kwargs.items()]) + ")"
            message = f"Calling {decorating(f.__name__, 32)}{arg}"
        else:
            message = f"+ {decorating(f.__name__, 32)}"

        if logger is None:
            logging.debug(message)
        else:
            logger.debug(message)

    return log


def log_exit(logger=None, logRets=False):
    def log(f, *args, **kwargs):
        if logRets:
            ret = " returned " + repr(kwargs['message_by_function'])
            message = f"{decorating(f.__name__, 31)}{ret}"
        else:
            message = f"- {decorating(f.__name__, 31)}"

        if logger is not None:
            logger.debug(message)
        else:
            logging.debug(message)

    return log


def log_full(logger=None):
    return bread(log_enter(logger, True), log_exit(logger, True))


def log_stack(logger=None):
    return bread(log_enter(logger), log_exit(logger))


def log_timer(logger=None):
    def begin(*args, **kwargs):
        return time.perf_counter()

    def end(*args, **kwargs):
        if logger is not None:
            logger.debug(f"for {decorating(time.perf_counter() - kwargs['message_by_begin'], 32)}s")
        else:
            logging.debug(f"for {decorating(time.perf_counter() - kwargs['message_by_begin'], 32)}s")

    return bread(begin, end)
