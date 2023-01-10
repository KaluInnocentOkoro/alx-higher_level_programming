#!/usr/bin/python3
"""Verify object class instance"""


def is_kind_of_class(obj, a_class):
    """ Checks if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class
    Args:
        obj (a_class): object whose instance is to be verified
        a_class (class): class object of obj
    return: True if obj is instance of a_class, False otherwise
    """
    return isinstance(obj, a_class)
