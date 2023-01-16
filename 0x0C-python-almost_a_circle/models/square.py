#!/usr/bin/python3
"""A square class"""
from rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates a Square object
        Args:
            size (int): size of square
            x (int)
            y (int)
            id (any)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the size of a Square object"""
        return self.size

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
