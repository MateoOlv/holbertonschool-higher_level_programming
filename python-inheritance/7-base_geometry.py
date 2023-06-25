#!/usr/bin/python3
"""Bsasegeometry class"""


class BaseGeometry:
    """BC"""
    def area(self):
        """raises exep"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
