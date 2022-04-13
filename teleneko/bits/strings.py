__all__ = ['decorating', 'transfer', 'str_type', 'str_val']

from typing import Union


def decorating(x: str, command: Union[int, str] = 30, default: Union[int, str] = 37):
    """
    Make string colorful

    Args:
        x: the string you want to decorate
        command: CSI command at the beginning
        default: CSI command at the end

    Returns: decorated string

    Examples:
        >>> decorating('qwq', 30, 37)
        qwq
       ^   ^
\033[30m   \033[37m
    """
    return f"\033[{str(command)}m{x}\033[{str(default)}m"


def transfer(x):
    """
    replace special character to escape character

    Args:
        x: the input string

    Returns: translated string

    Examples:
        >>> print('1\\n1')
        1
        1
        >>> print(transfer('1\\n1'))
        1\n1
    """
    x = x.replace('\n', decorating('\\n', 31, 33))
    x = x.replace('\r', decorating('\\r', 31, 33))
    x = x.replace('\t', decorating('\\t', 31, 33))

    return x


def str_type(x):
    """
    detect the type of x and return a printable string

    Args:
        x: input data

    Returns: type of x

    Examples:
        >>> str_type(123)
        int
        >>> str_type([])
        list
        >>> str_type(dict())
        dict<at 0xfffffffff>
    """
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
    """
    call __str__, and highlight string type
    Args:
        x: input object

    Returns: its __str__()

    """
    s = str(x)
    if isinstance(x, str):
        s = decorating("'" + transfer(s) + "'", 33)
    return s
