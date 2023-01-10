#!/usr/bin/pyhton3
""" A subclass of python list"""


class MyList(list):
    """A class that inherits from python list"""

    def print_sorted(self):
        """Method prints a list in sorted order (ascending sort"""
        print(sorted(self))
