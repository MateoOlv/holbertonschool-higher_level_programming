#!/usr/bin/python3

import unittest

max_integer = __import__("6-max_integer").max_integer
class TestMaxInteger(unittest.TestCase):
    def test1(self):
        """
        test max int with a ordered list"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test2(self):
        """
        test max int with a unordered list"""
        self.assertEqual(max_integer([4, 2, 3]), 4)

    def test6(self):
        """
        test max int with only one value
        """
        self.assertEqual((max_integer([4])), 4)

    def test3(self):
        """
        test max int with a negative value"""
        self.assertEqual(max_integer([1, 2, 3, 4, -4]), 4)

    def test4(self):
        """
        test max int with all negative values"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test5(self):
        """
        test max inte with a empty list
        """
        self.assertEqual(max_integer([]), None)

    def test7(self):
        """
        test max int with a string in the list
        """
        self.assertRaises(TypeError, max_integer, [1, "test", 4, 2])

    if __name__ == '__main__':
        unittest.main()
