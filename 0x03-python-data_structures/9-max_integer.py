#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or my_list == []:
        return None
    max_int = my_list[0]
    for num in my_list:
        if num > max_int:
            max_int = num
    return max_int
