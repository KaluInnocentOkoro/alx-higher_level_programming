#!/usr/bin/python3
def no_c(my_string):
    """function that removes all characters c and C from a string.
    Args:
        my_string (str)
    Returns: The updated string list
    """
    new_string = ""
    for ele in my_string:
        if ele == 'C' or ele == 'c':
            continue
        else:
            new_string += ele
    return new_string
