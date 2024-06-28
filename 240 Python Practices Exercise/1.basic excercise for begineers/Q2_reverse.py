"""Exercise 2: Write a Program to extract each digit from an integer in the reverse order.
"""

# n = input("ENter number : ")

# num = n[::-1]
# print("".join(num))


# Without using function
n = 12345
print(n//10)
reversed_n = 0
while n>0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n = n//10

print(reversed_n)