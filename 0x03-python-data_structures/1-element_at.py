#!/usr/bin/python3
def element_at(my_list, idx):
    """retrives an element from a list
    Args:
        my_list: (list)
        idx: (int) position of the element

    Returns: (list) my_list[idx] or None
    """
    if idx < 0 or idx > len(my_list):
        return None
    return my_list[idx]
