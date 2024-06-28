"""Excercise 6: Find the reverse of a number provided by the user(any number of digit)"""

n=int(input("enter the number: "))

reversed_n = 0

while(n>0):
    digit = n % 10 # 6 8 7 
    reversed_n = reversed_n * 10 + digit  #687
    n = n//10 # 7

print(reversed_n)