#!/usr/bin/python3
def is_same_class(obj, a_class):
    """function checks if obj is an instance of a_class
    Args:
        obj (any type):
        a_class:
    """
    return type(obj) is a_class
