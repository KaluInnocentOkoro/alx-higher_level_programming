#!/usr/bin/python3
"""Json Deserialization"""
import json


def load_from_json_file(filename):
    """Function  creates an Object from a JSON file
    Args:
        filename (any): file whose content is to be deserialized
    Returns: a python object
    """
    with open(filename, 'r', encoding="utf-8") as file:
        json_obj = json.load(file)
        return json_obj
