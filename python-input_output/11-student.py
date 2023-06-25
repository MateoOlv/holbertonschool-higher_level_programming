#!/usr/bin/python3
"""Student module"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """Inits"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """prints __dict__"""
        if(isinstance(attrs, list) and all(isinstance(x, str) for x in attrs)):
            return({x: y for x, y in self.__dict__.items() if x in attrs})
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        reloads attrs from json
        """

        for attr in json:
            setattr(self, attr, json.get(attr))
