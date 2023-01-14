#!/usr/bin/python3
"""Json serialization"""
import json


def to_json_string(my_obj):
    """Fucntion serializes a python object
    Args:
        my_obj (obj): python object to be serialized
    Returns: JSON representation of an object (string)
    """
    return json.dumps(my_obj)
