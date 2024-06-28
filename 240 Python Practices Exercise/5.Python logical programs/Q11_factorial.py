"""Excercise 11:Write a program that can find the factorial of a given number provided by the user"""

n=int(input("enter the number : "))
factorial=1

for i in range(1,n+1):
    factorial=factorial*i
print(factorial)