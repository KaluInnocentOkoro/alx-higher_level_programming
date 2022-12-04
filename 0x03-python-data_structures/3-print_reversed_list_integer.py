#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Function reverses a list
    Args:
        my_list: (list) list of elements to be reversed

    Returns: The list in reverse order
    """
    if my_list:
        for ele in my_list[::-1]:
            print("{:d}".format(ele))
