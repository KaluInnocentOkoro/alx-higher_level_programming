#!/usr/bin/python3
"""A base model"""


class Base:
    """Defines a Base class"""

    __nb_objects = 0

    def __int__(self, id=None):
        """Instantiates a new Base Object
        Args:
            id (int)
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
