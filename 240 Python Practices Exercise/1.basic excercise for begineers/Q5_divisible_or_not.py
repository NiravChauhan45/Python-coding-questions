"""Excercise 5: Write a program that will tell whether the given number is divisible by 3 & 6"""

num=int(input("enter the number "))

if (3 % num) == 0 and (6 % num) == 0:
    print("the number is divisible by 3 and 6")
else:
    print("the number is not divisible by 3 and 6")