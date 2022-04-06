import functools
import logging
import time

def clamper(begin = None, end = None):
    
    def decorator(f):
    
        @functools.wraps(f)
        def warpper(*args, **kargs):
            message = None
            
            if begin != None:
                message = begin(f, *args, **kargs)
            
            ret = f(*args, **kargs)
            
            if end != None:
                if message != None:
                    kargs['message_by_begin'] = message
                if ret != None:
                    kargs['message_by_function'] = ret
                
                end(f, *args, **kargs)
            
            return ret
        return warpper
    
    return decorator

def log_enter(logger = None):
    def log(f, *args, **kargs):
        if logger is None:
            logging.debug( f"Calling {f.__name__}({args}, {kargs})" )
        else: 
            logger.debug( f"Calling {f.__name__}({args}, {kargs})" )
    return log
    
def log_exit(logger = None):
    def log(f, *args, **kargs):
        if logger is None:
            logging.debug( f"{f.__name__} returned {kargs['message_by_function']}" )
        else: 
            logger.debug( f"{f.__name__} returned {kargs['message_by_function']}" )
    return log

def full_log(logger = None):
    return clamper( log_enter(logger), log_exit(logger) )
