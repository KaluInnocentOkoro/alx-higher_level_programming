#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Function replaces the element at a given position of a list
    Args:
        my_list: (list)
        idx: (int) position of the element to be replaced
        element: element to added

    Returns: The updated list
    """
    size = len(my_list)
    if idx >= 0 and idx <= size - 1:
        my_list[idx] = element
    return my_list
