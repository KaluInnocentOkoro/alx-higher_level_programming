#!/usr/bin/python3


def add_attribute(object, attribute, value):
    """Function adds a new attribute to an object
    Args:
        object (any): object to receiving attribute.
        attribute (str): attribute to be added.
        value (any): value of the attribute to be added.
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, value)
