#!/usr/bin/python3
"""Class"""


class MyList(list):
    """define prints sorted"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
