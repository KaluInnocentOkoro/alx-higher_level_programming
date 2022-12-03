#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    size = len(sys.argv)
    if size != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    operators = ['+', '-', '*', '/']
    if op in operators:
        if op == '+':
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
        if op == '-':
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        if op == '*':
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        if op == '/':
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
        sys.exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)