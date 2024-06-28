"""Excercise 9:Write a program to print whether a given number is prime number or not"""


num = int(input("Enter Number : "))

for i in range(2,num):
    if num % i == 0:
        print("it is not a prime number")
        break
else:
    print("it is prime number")

