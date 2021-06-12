# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-12 17:51:24
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-12 18:16:42

from art import logo

print(logo)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

cont = "y"

a = float(input("What's the first number? "))

while cont == "y":
    for op in operators:
        print(op)
    
    operator = input("Pick an operation: ")
    b = float(input("What's the next number? "))

    result = operators[operator](a, b)

    print(f"{a} {operator} {b} = {result}")

    cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    a = result