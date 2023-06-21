#!/usr/bin/python3
"""Define read file"""


def read_file(filename=""):
    """Open file and read"""
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
