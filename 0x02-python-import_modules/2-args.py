#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv)
    if size - 1 == 0:
        print("{} arguments.".format(size - 1))
    elif size - 1 == 1:
        print("{} argument:".format(size - 1))
        print("{}: {}".format(size - 1, sys.argv[1]))
    else:
        print("{} arguments:".format(size - 1))
        for idx in range(1, size):
            print("{}: {}".format(idx, sys.argv[idx]))
