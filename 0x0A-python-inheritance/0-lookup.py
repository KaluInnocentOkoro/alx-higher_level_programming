#!/usr/bin/python3
"""Object Methods"""


def lookup(obj):
    """Function returns object attributes and methods
    Args:
        obj (class):
    Returns: list of object Attributes
    """
    return dir(obj)
