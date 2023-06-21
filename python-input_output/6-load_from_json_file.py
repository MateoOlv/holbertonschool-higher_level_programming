#!/usr/bin/python3
"""def load from json file"""
import json


def load_from_json_file(filename):
    """reads and return f"""
    with open(filename, mode='r', encoding='utf-8') as f:
        return (json.load(f))
