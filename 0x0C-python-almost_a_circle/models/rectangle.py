#!/usr/bin/python3
"""A Rectangle class"""
from base import Base


class Rectangle(Base):
    """Defines a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates a Rectangle object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieves the width of a Rectangle object"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of a rectangle object
        Args:
            value (int): value of rectangle width
        """
        self.__width = value

    @property
    def height(self):
        """retrieves the height of a rectangle object"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of a rectangle height
        Args:
            value (int): value of rectangle height
        """
        self.__height = value

    @property
    def x(self):
        """retrieves the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        self.__x = value

    @property
    def y(self):
        """retrieves the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        self.__y = value
