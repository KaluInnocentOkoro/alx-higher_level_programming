#!/usr/bin/python3
"""prints a square"""


def print_square(size):
    """Prints a square with the character '#'
    Args:
        size (int): size of the sides of the square
    """
    if size >= 0:
        if isinstance(size, int):
            for i in range(size):
                print("#" * size)
        else:
            raise TypeError("size must be an integer")
    else:
        raise ValueError("size must be >= 0")
