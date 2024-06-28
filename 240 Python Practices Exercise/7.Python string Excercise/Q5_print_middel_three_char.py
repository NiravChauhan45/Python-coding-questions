"""Exercise 5: Write a program to create a new string made of the middle three characters of an input
string.
"""

name = 'jaSonAy'

l = len(name)

c = l//2
x = name[c-1]
y = name[c]
z = name[c+1]

result = "".join([x,y,z])
print(result)