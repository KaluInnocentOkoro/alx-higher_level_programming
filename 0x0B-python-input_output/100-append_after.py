#!/usr/bin/python3
"""appends a text"""


def append_after(filename="", search_string="", new_string=""):
    """Function inserts a line of text to a file,
    after each line containing a specific string
    Args:
        filename (txt): file to be appended to
        search_string (str): string to be searched
        new_string (str): string to be appended
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
