"""Excercise 7: Write a program that will check whether the number is armstrong number or not."""

num = int(input("Enter number : "))

a = num % 10
x = num // 10

b = x % 10
c = x // 10


if num == (a**3 + b**3 + c**3):
    print("This is armstrong")
else:
    print("This is not armstrong")