#!/usr/bin/python3
import json
"""Def from json string"""


def from_json_string(my_str):
    """return object represented by a json string"""
    return (json.load(my_str))
