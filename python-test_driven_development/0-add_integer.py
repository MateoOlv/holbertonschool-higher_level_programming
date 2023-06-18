#!/usr/bin/python3
"""
define add integer
"""


def add_integer(a, b=98):
    """
    do the math
    """
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    elif (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    else:
        return int(a)+int(b)
