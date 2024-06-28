"""
Exercise 2: Print characters from a string that are present at an even index number

Write a program to accept a string from the user and display characters that are present at an even index
number.

For example, str = "pynative" so you should display 'p','n','t','v'.
"""

string = input("enter the text: ")
x = list(string)
print(x[0::2])