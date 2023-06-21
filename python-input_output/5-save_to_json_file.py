#!/usr/bin/python3
"""Define save to json file"""
import json


def save_to_json_file(my_obj, filename):
    """Opnes the file in writing mode and write"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
