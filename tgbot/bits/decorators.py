from tgbot.bits.strings import decorating, str_type
import functools
import logging
import time
from tgbot import is_debug


def bread(begin=None, end=None, exp=None):
    def decorator(f):

        @functools.wraps(f)
        def wrapper(*args, **kwargs):

            if begin is not None:
                message = begin(f, *args, **kwargs)
            else:
                message = None
            try:
                ret = f(*args, **kwargs)
            except Exception as e:
                exp(e)
                raise e

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
    def log_debug(f, *args, **kwargs):
        if logArgs:
            arg = "(" + ", ".join([repr(x) for x in args] + [f"{k}={v!r}" for k, v in kwargs.items()]) + ")"
            message = f"Calling {decorating(f.__name__, 32)}{arg}"
        else:
            message = f"+ {decorating(f.__name__, 32)}"

        if logger is not None:
            logging.debug(message)
        else:
            print(message)

    if is_debug:
        return log_debug


def log_exit(logger=None, logRets=False):
    def log_debug(f, *args, **kwargs):
        if logRets:
            ret = " returned " + repr(kwargs['message_by_function'])
            message = f"{decorating(f.__name__, 31)}{ret}"
        else:
            message = f"- {decorating(f.__name__, 31)}"

        if logger is not None:
            logger.debug(message)
        else:
            print(message)

    if is_debug:
        return log_debug


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
            print(f"for {decorating(time.perf_counter() - kwargs['message_by_begin'], 32)}s")

    if is_debug:
        return bread(begin, end)
    else:
        return bread()


def log_exceptions(logger=None):
    def log_error(e):
        if logger is not None:
            logger.error(decorating(f"{str_type(e)} : {e}", 31))
        else:
            print(decorating(f"{str_type(e)} : {e}", 31))

    return bread(exp=log_error)


def handle(*events):
    def decorator(f):

        for e in events:
            e.hock(f)

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        return wrapper

    return decorator
