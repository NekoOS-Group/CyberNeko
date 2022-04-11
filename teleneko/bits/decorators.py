import functools
import time
import typing
from typing import Union, List, Tuple

from .strings import decorating, str_type

__all__ = ['log_full', 'log_stack', 'log_timer', 'log_exceptions', 'with_info', 'handle']


# bread is very delicious
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
                if exp is not None:
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


def log_enter(logger=None, logArgs: bool = False, debug: bool = False):
    def log_debug(f, *args, **kwargs):
        if logArgs:
            arg = "(" + ", ".join([repr(x) for x in args] + [f"{k}={v!r}" for k, v in kwargs.items()]) + ")"
            message = f"Calling {decorating(f.__name__, 32)}{arg}"
        else:
            message = f"+ {decorating(f.__name__, 32)}"

        if logger is not None:
            logger.debug(message)
        else:
            print(message)

    if debug:
        return log_debug


def log_exit(logger=None, logRets: bool = False, debug: bool = False):
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

    if debug:
        return log_debug


def log_full(logger=None, debug: bool = False):
    return bread(log_enter(logger, True, debug=debug), log_exit(logger, True, debug=debug))


def log_stack(logger=None, debug: bool = False):
    return bread(log_enter(logger, debug=debug), log_exit(logger, debug=debug))


def log_timer(logger=None, debug: bool = False):
    def begin(*args, **kwargs):
        return time.perf_counter()

    def end(*args, **kwargs):
        if logger is not None:
            logger.debug(f"for {decorating(time.perf_counter() - kwargs['message_by_begin'], 32)}s")
        else:
            print(f"for {decorating(time.perf_counter() - kwargs['message_by_begin'], 32)}s")

    if debug:
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


def with_info(handler, begin=None, end=None, report_params: bool = False):
    def info_begin(f, *args, **kwargs):
        if begin is not None:
            if report_params:
                handler(begin, *args, **kwargs)
            else:
                handler(begin)

    def info_end(f, *args, **kwargs):
        if end is not None:
            if report_params:
                handler(end, *args, **kwargs)
            else:
                handler(end)

    return bread(info_begin, info_end)


from .controller import event


def handle(*events: event):
    def decorator(f):
        for e in events:
            e.hock(f)

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        return wrapper

    return decorator


def with_return(_type: Union[type, List[typing.Any], Tuple[typing.Any]]):
    def wrapper(f):
        def new_f(*args, **kwargs) -> _type:
            ret = f(*args, **kwargs)
            if type(ret) == _type:
                return ret
            else:
                return _type(ret)

        return new_f

    return wrapper
