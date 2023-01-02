#!/usr/bin/python3
"""A Rectangle class"""


class Rectangle:
    """Defines a Rectangle class"""

    def __init__(self, width=0, height=0):
        """Instantiates a Rectangle object
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Initializes the width of the rectangle object
        Args:
            value (int): value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the value of the height of the Rectangle object"""
        return self.__height

    @height.setter
    def height(self, value):
        """initializes the height of the rectangle object
        Args:
            value (int): value of the height of rectangle object
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes and returns the area of a rectangle object"""
        return self.__width * self.__height

    def perimeter(self):
        """computes and returns the perimeter of rectangle object"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints the rectangle object with '#'"""
        my_rect = []
        for idx in range(0, self.__height):
            my_rect.append("#" * self.__width)
        return "\n".join(my_rect)
