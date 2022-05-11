__all__ = [
    'decorating',
    'transfer',
    'str_type',
    'str_val'
]

from .typing import *


def decorating(
        x: str,
        command: Union[int, str] = 30,
        default: Union[int, str] = 37
) -> str:
    """Make string colorful

    Args:
        x: the string to be decorated
        command: CSI command at the beginning
        default: CSI command at the end

    Returns:
         decorated string
    """
    return f"\033[{str(command)}m{x}\033[{str(default)}m"


def transfer(
        x: str
) -> str:
    """replace special character to escape character

    Args:
        x: the input string

    Returns:
        translated string

    Examples:
        >>> print('1\\n1')
        1
        1
        >>> transfer('1\\n1')
        1\\n1
    """
    x = x.replace('\n', decorating('\\n', 31, 33))
    x = x.replace('\r', decorating('\\r', 31, 33))
    x = x.replace('\t', decorating('\\t', 31, 33))

    return x


def str_type(
        x: Any,
        origin: bool = False
) -> str:
    """detect the type of x and return a printable string

    Args:
        x: input data
        origin: not colored

    Returns:
        string of type of x
    """
    s = str(type(x)).split("'")[1]
    if type(x) is list:
        return decorating("list[%d]" % len(x), 34)
    elif type(x) in [int, float, bool]:
        return decorating(s, 36)
    elif type(x) is str:
        return decorating(s, 33)
    elif isinstance(x, BaseException):
        return s
    else:
        s = s.split('.')[-1]
        if not origin:
            s = decorating("%s<at %s>" % (s, hex(id(x))), '30;47', '0;37')
    return s


def str_val(
        x: Any,
        origin: bool = False
) -> str:
    """
    If x is a string, then return string 'x' with color 33.

    Others return x.__str__()

    Args:
        origin:
        x: input object

    Returns:
        string format of x

    """
    if origin:
        return repr(x)
    s = str(x)
    if isinstance(x, str):
        s = decorating("'" + transfer(s) + "'", 33)
    return s
