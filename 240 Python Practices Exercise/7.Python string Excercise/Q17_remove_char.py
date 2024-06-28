"""
Exercise 17: Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'
expected-->2510
"""

str1 = 'I am 20 years and 6 months old'

str2 = str1.split()

new = []

for i in str2:
    if i.isdigit() == True:
        new.append(i)

print(" ".join(new))