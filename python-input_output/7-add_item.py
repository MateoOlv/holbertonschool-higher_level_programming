#!/usr/bin/python3
"""imports"""
import sys
import os
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.isfile("add_item.json"):
    list = load_from_json_file("add_item.json")
else:
    list = []
save_to_json_file(list + sys.argv[1:], "add_item.json")
