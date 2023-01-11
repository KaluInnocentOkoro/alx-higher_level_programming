#!/usr/bin/python3
"""A Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry"""

    def __int__(self, width, height):
        """Instantiates a Rectangle object
        Args:
            width (int): Rectangle width
            height (int): Height of Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
