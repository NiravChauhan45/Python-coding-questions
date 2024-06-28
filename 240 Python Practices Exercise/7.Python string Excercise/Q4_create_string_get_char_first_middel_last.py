"""Exercise 4: Create a string made of the first, middle and last character

Write a program to create a new string made of an input string’s first, middle, and last character.
"""

name = input("Enter your name : ")

a = name[0]

l = len(name)
x = int(l//2)

b = name[x]
c = name[-1]

print(",".join([a,b,c]))
