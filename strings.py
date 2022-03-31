def decorating(x, color=30):
    return "\033[%dm%s\033[37m" % (color, x)

def str_type(x):
    s = str(type(x)).split("'")[1]
    if s == 'list':
        s = decorating( "list[%d]" % len(x), 34 )
    elif s == 'int' or s=='float':
        s = decorating(s, 36)
    elif s == 'str':
        s = decorating(s, 33)
    else:
        s = s.split('.')[-1]
        s = "%s<at %s>" % (s,hex(id(x)))
    return s
