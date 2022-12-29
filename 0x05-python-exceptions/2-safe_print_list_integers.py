#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for idx in range(x):
            if type(my_list[idx]) is int:
                print("{:d}".format(my_list[idx]), end="")
                count += 1
            else:
                continue
    except ValueError:
        pass
    print()
    return count
