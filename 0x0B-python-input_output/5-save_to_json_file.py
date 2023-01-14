#!/usr/bin/python3
"""serialization to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Function writes an Object to a text file, using a JSON representation
    Args:
        my_obj (obj): object to be serialized to file
        filename (txt): file to be written to
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
