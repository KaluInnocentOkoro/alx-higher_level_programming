#!/usr/bin/python3
"""script adds all arguments to a Python list, and then save them to a file"""
import sys


if __name__ == "__main__":
    load_from_json_file =\
        __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    args = sys.argv[1:]
    file_name = "add_item.json"

    try:
        content = load_from_json_file(file_name)
    except FileNotFoundError:
        content = []
    content.extend(args)
    save_to_json_file(content, file_name)
