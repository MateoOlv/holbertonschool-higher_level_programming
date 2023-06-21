#!/usr/bin/python3
"""Def from json string"""
import json



def from_json_string(my_str):
    """return object represented by a json string"""
    return (json.load(my_str))
