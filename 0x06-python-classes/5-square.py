#!/usr/bin/python3
"""Describes a square class"""


class Square:
    """Defines a square object"""
    def __init__(self, size=0):
        """initializes an instance of the square class
        Args:
            size (int): size of the square
        """
        self.__size = size

    def area(self):
        """defines the area of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square
        Args:
            value (int): value of the square size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Public instance method that prints the square with to stdout
        """
        if self.__size == 0:
            print()
        else:
            for idx in range(self.__size):
                print("#" * self.__size)
