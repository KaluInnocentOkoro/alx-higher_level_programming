#!/usr/bin/python3
"""A Square Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initializes a new instance of a Square object
        Args:
            size (int): Size of a square object
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
