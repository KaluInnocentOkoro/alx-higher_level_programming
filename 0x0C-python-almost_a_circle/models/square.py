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

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes
        Args:
            args (list or tuple)
            kwargs (dict)
        """
        if args and len(args):
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.width = value
                elif key == 2:
                    self.height = value
                elif key == 3:
                    self.x = value
                elif key == 4:
                    self.y = value
        else:
            if kwargs and len(kwargs):
                if "id" in kwargs:
                    self.id = kwargs["id"]
                elif "width" in kwargs:
                    self.width = kwargs["width"]
                elif "height" in kwargs:
                    self.height = kwargs["height"]
                elif "x" in kwargs:
                    self.x = kwargs["x"]
                elif "y" in kwargs:
                    self.y = kwargs["y"]
