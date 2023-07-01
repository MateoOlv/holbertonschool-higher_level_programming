#!/usr/bin/python3
"""inherits Base"""

from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None 
    
    """Property of all"""


    @property
    def width(self):
        """get value width"""
        return self.__width
    @property
    def height(self):
        """get value height"""
        return self.__height
    @property
    def x(self):
        """get value x"""
        return self.__x
    @property
    def y(self):
        """get value y"""
        return self.__y

    """Setters of all"""


    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value
