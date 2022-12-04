#!/usr/bin/python3
def element_at(my_list, idx):
    """retrives an element from a list
    Args:
        my_list: (list)
        idx: (int) position of the element to be retrieved

    Returns: my_list[idx] or None
    """
    size = len(my_list)
    if idx > size or idx < 0:
        return None
    return my_list[idx]
