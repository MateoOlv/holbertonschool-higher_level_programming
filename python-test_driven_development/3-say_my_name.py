#!/usr/bin/python3
"""
Define Error handler
"""


def Error(first_name, last_name):
    """
    Error cases
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")


"""Define say my name"""


def say_my_name(first_name, last_name=""):
    """
    Call Error handler
    And
    Print the name with the last name
    """
    Error(first_name, last_name)
    print("My name is {} {}". format(first_name, last_name))
