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

    def to_json(self):
        """Retrieves a dictionary reprsentation of a student instance"""
        return self.__dict__
