#!/usr/bin/python3
"""JSON deserialization"""
import json


def from_json_string(my_str):
    """Deserializes a json string
    Args:
        my_str (str): string to be deserialized
    Returns: object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
