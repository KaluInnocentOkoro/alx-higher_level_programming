#!/usr/bin/python3
"""reading a file"""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename (txt): file to be read
    """
    with open(filename, encoding="utf-8") as file:
        f = file.read()
        print(f)
