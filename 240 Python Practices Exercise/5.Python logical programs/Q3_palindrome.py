"""Exercise 3:Write a program to check if the given number is a palindrome number."""

num = input("Enter number : ")

reverse = num[::-1]

if num == reverse:
    print("This is palindrome number")
else:
    print("This is not palindrome number")