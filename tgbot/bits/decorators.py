from tgbot.bits.strings import decorating
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

def log_enter(logger = None, logArgs = False):
    def log(f, *args, **kargs):
        message = ""
        if logArgs:
            arg = "(" + ", ".join([repr(x) for x in args] + [f"{k}={v!r}" for k, v in kargs.items()]) + ")"
            message = f"Calling {decorating(f.__name__, 32)}{arg}"
        else:
            message = f"+ {decorating(f.__name__, 32)}"
        
        if logger == None:
            logging.debug(message)
        else: 
            logger.debug(message)
    return log
    
def log_exit(logger = None, logRets = False):
    def log(f, *args, **kargs):
        message = ""
        if logRets:
            ret = " returned " + repr(kargs['message_by_function'])
            message = f"{decorating(f.__name__, 31)}{ret}"
        else:
            message = f"- {decorating(f.__name__, 31)}"
        
        if logger == None:
            logging.debug(message)
        else: 
            logger.debug(message)
    return log

def log_full(logger = None):
    return clamper( log_enter(logger, True), log_exit(logger, True) )
    
def log_stack(logger = None):
    return clamper( log_enter(logger), log_exit(logger) )
    
def log_timer(logger = None):
    def begin(*args, **kargs):
        return time.perf_counter()
    
    def end(*args, **kargs):
        if logger == None:
            logging.debug( f"for {decorating(time.perf_counter() - kargs['message_by_begin'], 32)}s" )
        else:
            logger.debug( f"for {decorating(time.perf_counter() - kargs['message_by_begin'], 32)}s" )
    
    return clamper( begin, end )

