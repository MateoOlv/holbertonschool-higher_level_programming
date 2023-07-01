#!/usr/bin/python3
"""Imports and module"""
import json
from os import path


class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id == None:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
        else:
            self.id = id
