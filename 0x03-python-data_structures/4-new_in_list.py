#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Function replaces an element at a specific position
    without modifying the original list
    Args:
        my_list: (list)
        idx: The required position
        element: element to be replaced
    Returns: A new list
    """
    size = len(my_list)
    if idx > size or idx < 0:
        return my_list
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
