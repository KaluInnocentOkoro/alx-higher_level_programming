#!/usr/bin/python3
"""check for subclasses"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherited
    (directly or indirectly from a specified class
    Args:
        obj (a_class):
        a_class (class):
    return:
    True if obj is an instance of an inherited class, False otherwise
        """
    return not type(obj) is a_class and issubclass(type(obj), a_class)
