# https://github.com/MaxHyken/lab11-MH-RP/
# Partner 1: Max Hyken
# Partner 2: Rafael Penhas

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except:
        if a < 0:
            raise ValueError

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):

    if a == 0:
        raise ZeroDivisionError

    return b/a

def log(a, b):
    if b <= 0:
        raise ValueError
    
    return math.log(b, a)

def exp(a, b):
    return a ** b


