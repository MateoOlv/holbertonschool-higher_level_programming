#!/usr/bin/python3
"""Define inherits_from"""


def inherits_from(obj, a_class):
    """check the type of obj """
    if type(obj) == a_class:
        return (False)
    else:
        return (isinstance(obj, a_class))
