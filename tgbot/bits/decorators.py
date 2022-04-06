def clamper(begin = None, end = None):
    
    def decorator(f):
    
        @functools.wraps(f)
        def warpper(*args, **kargs):
            message = None
            
            if begin != None:
                message = begin(*args, **kargs)
                
            ret = f(*args, **kargs)
            
            if end != None:
                if message != None:
                    kargs['message_by_begin'] = message
                if ret != None:
                    kargs['message_by_function'] = ret
                
                end(*args, **kargs)
            
            return ret
        return warpper
    
    return decorator

def log_enter(logger):
    pass
    
def log_exit(logger):
    pass
