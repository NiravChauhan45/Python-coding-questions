"""Excercise 10: how does finally block work in python"""

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")
finally:
    print("Hip Hip hurray!!")