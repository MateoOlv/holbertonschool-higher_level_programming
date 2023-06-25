#!/usr/bin/python3
"""imports"""
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if path.isfile("add_item.json"):
    list = load_from_json_file("add_item.json")
else:
    list = []
save_to_json_file(list + argv[1:], "add_item.json")
