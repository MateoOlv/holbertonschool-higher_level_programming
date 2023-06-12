#!/usr/bin/python3
""" Define class """


class Square:
    """Define init."""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position
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

    """define position property"""
    @property
    def position(self):
        return (self.__position)
    """Define position setter"""
    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = (value[0], value[1])
    """Define myprint"""

    def my_print(self):
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
        if self.size == 0:
            print("")
            return
