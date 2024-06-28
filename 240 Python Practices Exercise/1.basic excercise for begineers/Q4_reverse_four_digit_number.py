"""Excercise 4: Write a program that will reverse a four digit number.Also it checks whether the reverse"""

num = int(input("Enter your number : "))
reversed_n = 0

while num > 0:
    val = num % 10
    reversed_n = reversed_n * 10 + val
    num //=10

if num==reversed_n:
 print(reversed_n, True)
else:
 print(reversed_n, False)