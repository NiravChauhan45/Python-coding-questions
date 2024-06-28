"""Excercise 2: Write a python program to search a given number from a list"""

l1 = [45,18,3,33,12,10,17,333]

num = input("Enter number: ")
for i in l1:
    if i in l1:
        print("Number exist")
        break
    else:
        print("number dont exist")