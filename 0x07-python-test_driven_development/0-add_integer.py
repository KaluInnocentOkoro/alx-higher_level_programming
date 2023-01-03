#!/usr/bin/python3
"""Function adds integers"""


def add_integer(a, b=98):
    """add 2 integers
    Args:
        a (int): integer 2
        b (int): integer 2
    Returns:
        a + b
    """
    if isinstance(a, int) or isinstance(a, float):
        if isinstance(b, int) or isinstance(b, float):
            return int(a + b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
