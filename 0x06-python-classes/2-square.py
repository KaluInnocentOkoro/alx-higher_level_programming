#!/usr/bin/python3
"""Describes a square class"""


class Square:
    """Defines a square object"""
    def __init__(self, size=0):
        """initializes an instance of the square class
        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
