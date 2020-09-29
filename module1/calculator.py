#! /bin/bash/python

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("please enter operation: +, -, /, *, mod, pow, div")

def mod(a, b):
    if b != 0:
        print(a % b)
    else:
        print("Деление на 0!")

def pow(a, b):
    print(a ** b)

def div(a, b):
    if b != 0:
        print(a // b)
    else:
        print("Деление на 0!")

def mult(a, b):
    print(a * b)

def division(a, b):
    if b != 0:
        print(a / b)
    else:
        print("Деление на 0!")

def add(a, b):
    print(a + b)

def sub(a, b):
    print(a - b)

if operation == "+":
    add(a, b)
elif operation == "-":
    sub(a, b)
elif operation == "/":
    division(a, b)
elif operation == "*":
    mult(a, b)
elif operation == "mod":
    mod(a, b)
elif operation == "pow":
    pow(a, b)
elif operation == "div":
    div(a, b)



