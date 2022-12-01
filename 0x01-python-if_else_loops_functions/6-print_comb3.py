#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i % 10, j % 10))
        else:
            print("{}{}, ".format(i % 10, j % 10), end="")
