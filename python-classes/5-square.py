#!/usr/bin/python3
""" Define class """


class Square:
    """Define init."""

    def __init__(self, size=0):
        self.__size = size
    """Define size property"""
    @property
    def size(self):
        return (self.__size)
    """Define size"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise (TypeError("size must be an integer"))
        if value < 0:
            raise (ValueError("size must be >= 0"))
        self.__size = value

    """Define area"""

    def area(self):
        return (self.__size**2)

    """Define myprint"""

    def my_print(self):
        for i in range(self.size):
            for i in range(self.size):
                print("#", end="")
            print()
        if self.size == 0:
            print("")
