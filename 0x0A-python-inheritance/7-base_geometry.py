#!/usr/bin/python3
"""A Base class"""


class BaseGeometry:
    """A BaseGeometry class """

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method validates values
        Args:
            name (str):
            value (int):
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
