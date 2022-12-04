#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        a1 = tuple_a[0]
        b1 = tuple_a[1]
    elif len(tuple_a) == 1:
        a1 = tuple_a[0]
        b1 = 0
    else:
        a1 = 0
        b1 = 0
    if len(tuple_b) >= 2:
        a2 = tuple_b[0]
        b2 = tuple_b[1]
    elif len(tuple_b) == 1:
        a2 = tuple_b[0]
        b2 = 0
    else:
        a2 = 0
        b2 = 0
    a = a1 + a2
    b = b1 + b2
    return (a, b)
