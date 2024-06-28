"""
Exercise 14: Split a string on hyphens
Write a program to split a given string on hyphens and display each substring.
str1 = Emma-is-a-data-scientist
Expected-->Displaying each substring
"""

str1 = "Nirav-is-a-data-engineer"
str2 = str1.split('-')

for i in str2:
    print(i)