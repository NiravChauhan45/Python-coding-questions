"""Excercise 6: Write a program that will take three digits from the user and add the square of each
digit."""

num = int(input("Enter three digit number : "))

a = num % 10
x = num // 10
b = x%10
c = x//10

output_value = c**2 + b**2 + a**2
print(output_value)
