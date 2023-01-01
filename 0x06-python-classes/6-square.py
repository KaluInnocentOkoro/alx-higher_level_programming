#!/usr/bin/python3
"""Describes a square class"""


class Square:
    """Defines a square object"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes an instance of the square class
        Args:
            size (int): size of the square
            postion (tuple): coordinates of tge square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """retrieves the position property
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of position attribute
        Args:
            value (tuple): A tuple of 2 integers
        """
        if len(value) != 2 or \
                not isinstance(value, tuple) or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
                    raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def my_print(self):
        """Public instance method that prints the square with to stdout
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for idx in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)
