#!/usr/bin/python3
"""A base model"""


class Base:
    """Defines a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiates a Base object
        Args:
            id (int)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

