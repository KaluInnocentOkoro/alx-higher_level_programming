#!/usr/in/pyhton3
""" A subclass of python list"""


class MyList(list):
    """A class that inherits from python list"""

    def print_sorted(self):
        """prints a sorted list of items"""
        print(sorted(self))
