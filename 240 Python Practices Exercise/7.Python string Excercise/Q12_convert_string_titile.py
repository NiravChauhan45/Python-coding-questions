"""Excercise 12: Write a python program to convert a string to title case without using the title()"""

a = input("Enter string : ")
b = a.split()

r = '' 
for i in b:
    r = r+i.capitalize()+ " " 
    print(r) 