#!/usr/bin/python3
"""Geometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Method initializes an instance of a Rectangle object
        Args:
            width (int): Width of the Rectangle object
            height (int): Height of the Rectangle object
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method computes the area of a Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Method returns a description of the rectangle"""
        return "[{}] {}/{}".format(
            self.__class__.__name__,
            self.__width,
            self.__height)
