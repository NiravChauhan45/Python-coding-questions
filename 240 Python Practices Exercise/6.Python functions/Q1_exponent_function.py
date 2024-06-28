"""
Exercise 1: Write a function called exponent(base, exp) that returns an int value of base raises to the
power of exp.

Note here exp is a non-negative integer, and the base is an integer.
"""

def exponent(base,exp):
    result=pow(base,exp)
    print(result)

exponent(10,2)