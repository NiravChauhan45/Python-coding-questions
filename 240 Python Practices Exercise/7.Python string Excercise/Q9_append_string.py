"""
Exercise 8: Append new string in the middle of a given string
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
s1 = "Ault"
s2 = "Kelly"
expected-->AuKellylt
"""

s1 = "Ault"
s2 = "Kelly"

le = len(s1)
mid = le//2
f=s1[:mid]
l=s1[mid:]

s3 = f + s2 + l
print(s3)