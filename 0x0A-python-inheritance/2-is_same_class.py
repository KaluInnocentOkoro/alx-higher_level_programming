#!/usr/bin/python3
"""Check object instances"""


def is_same_class(obj, a_class):
    """ Checks if the object is exactly an instance of the specified class
    Args:
        obj (a_class): object to be verified
        a_class (class): The class of te given object

    return: True if ob is an instance of a_class, False otherwise
    """
    return True if type(obj) is a_class else False
