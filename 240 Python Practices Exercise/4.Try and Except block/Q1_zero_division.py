"""Excercise 1: Let see handling zero division exceptional error"""

try:
 print(5/0)
except ZeroDivisionError:
 print("you cant divide by zero")