#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(args[0], args[1])
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        result = None
    return result
