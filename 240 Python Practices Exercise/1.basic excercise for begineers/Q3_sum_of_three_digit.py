"""Excercise 3: Write a program that will give you the sum of 3 digits"""

x=int(input("enter three digit number : "))

a = x%10
x = x//10

b = x%10
c = x//10

print(f"{a+b+c}")