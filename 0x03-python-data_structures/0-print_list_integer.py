#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """function that prints all integers of a list.
    Args:
        my_list: A list of integers

    Returns: Nothing
    """
    for ele in my_list:
        print("{:d}".format(ele))
