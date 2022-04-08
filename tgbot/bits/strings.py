__all__ = ['decorating', 'transfer', 'str_type', 'str_val']


def decorating(x, command=30, default=37):
    return "\033[%sm%s\033[0m\033[%sm" % (str(command), x, str(default))


def transfer(x):
    x = x.replace('\n', decorating('\\n', 31, 33))
    x = x.replace('\r', decorating('\\r', 31, 33))
    return x


def str_type(x):
    s = str(type(x)).split("'")[1]
    if s == 'list':
        s = decorating("list[%d]" % len(x), 34)
    elif s in ['int', 'float', 'bool']:
        s = decorating(s, 36)
    elif s == 'str':
        s = decorating(s, 33)
    elif isinstance(x, BaseException):
        s = s
    else:
        s = s.split('.')[-1]
        s = decorating("%s<at %s>" % (s, hex(id(x))), '30;47')
    return s


def str_val(x):
    s = str(x)
    if isinstance(x, str):
        s = decorating("'" + transfer(s) + "'", 33)
    return s
