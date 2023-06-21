#!/usr/bin/python3
"""def load from json file"""
import json


def load_from_json_file(filename):
    """reads and write loads of f"""
    with open(filename, mode='r', encoding='utf-8') as f:
        f.write(json.loads(f))
