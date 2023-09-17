#!/usr/bin/python3
import sys


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return f"Can't divid by zero"
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    should_continue = True
    num1 = float(input("What is the first number?: "))

    while should_continue:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation from the line above: ").strip()
        num2 = float(input("What is the next number?: "))

        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result:0.2f}")

        another_calc = input(f"Type 'y' to continue calculating with {result:0.2f}, or type 'n' to start a new calculation: ").lower().strip()
        num1 = result
        if another_calc != 'y':
            should_continue = False
            sys.stdout.write("\033c")
            sys.stdout.flush()
            calculator()


calculator()