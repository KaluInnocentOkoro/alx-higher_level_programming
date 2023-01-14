#!/usr/bin/python3
"""dict object"""


def class_to_json(obj):
    """Function dictionary description with simple data structure
     (list, dictionary, string, integer and boolean)
     for JSON serialization of an object
     Args:
         obj (obj):
     """
    return obj.__dict__
