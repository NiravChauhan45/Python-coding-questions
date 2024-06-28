"""Exercise 1: Check file is empty or not,Write a program to check if the given file is empty or not"""


import os

size = os.stat("240 Python Practices Exercise/3.File and exceptions/text_file.txt").st_size

if size == 0:
    print("file is empty")
else:
    print("file is not empty")