#!/usr/bin/python3
"""Writing to files"""


def write_file(filename="", text=""):
    """Function writes a string to a text file (UTF8)
    Args:
        filename (any): file to be written to
        text (txt): string to be written to file
    Returns: returns the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        f = file.write(text)
        return f
