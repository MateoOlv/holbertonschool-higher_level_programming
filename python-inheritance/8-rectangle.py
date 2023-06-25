#!/usr/bin/python3
"""Bsasegeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Class rectangle"""


class Rectangle(BaseGeometry):
    """creates rectangle class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
