#!/usr/bin/python3
def remove_char_at(str, n):
    idx = len(str)
    str1 = ""
    for i in range(idx):
        if i == n:
            continue
        else:
            str1 += str[i]
    return str1
