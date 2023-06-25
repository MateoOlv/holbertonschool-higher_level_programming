#!/usr/bin/python3
"""append write a"""


def append_write(filename="", text=""):
        with open(filename, mode="a", encoding="utf-8") as f:
                return f.write(text)