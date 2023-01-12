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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description"""
        return "[{}] {}/{}".format(
            self.__class__.__name__,
            self.__width,
            self.__height)
