#!/usr/bin/python3
"""A student Class"""


class Student:
    """Defines a Student"""

    def __init__(self, first_name, last_name, age):
        """Instantiates a student object
        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a student instance
        Args:
            attrs (list)
        """
        if type(attrs) is list and all(type(ele) is str for ele in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
