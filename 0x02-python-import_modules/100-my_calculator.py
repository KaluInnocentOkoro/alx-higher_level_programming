#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    size = len(argv)
    if size < 4 or size > 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if size == 4:
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]
        operators = {'+': add, '-': sub, '*': mul, '/': div}
        if op in operators:
            ans = operators[op](a, b)
            print("{} {} {} = {}".format(a, op, b, ans))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
