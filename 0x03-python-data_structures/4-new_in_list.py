#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    new_list = my_list[:]
    if idx > size or idx < 0:
        return new_list
    new_list[idx] = element
    return new_list
