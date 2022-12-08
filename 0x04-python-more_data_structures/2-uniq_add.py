#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    seq = set(my_list)
    for item in seq:
        add += item
    return add