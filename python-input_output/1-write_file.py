#!/usr/bin/python3
"""write file w"""


def write_file(filename="", text=""):
        with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(text)