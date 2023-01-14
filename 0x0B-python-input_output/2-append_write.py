#!/usr/bin/python3
"""appending to files"""


def append_write(filename="", text=""):
    """Function appends a string at the end of a text file (UTF8)
    Args:
        filename (any): file to be appended to
        text (txt): text to be appended
    Returns: the number of bytes of text appended
    """
    with open(filename, 'a', encoding="utf-8") as file:
        f = file.write(text)
        return f
