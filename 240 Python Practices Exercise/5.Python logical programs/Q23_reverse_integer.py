"""Exercise 23: Reverse a given integer number"""

# Method - 1
num = int(input("Enter number : "))
reversed_n = 0

while(num>0):
    digit = num % 10
    reversed_n = (reversed_n * 10) + digit
    num = num // 10

print(f"output of method - 1 is {reversed_n}")


# Method - 2
num = int(input("Enter number : "))

x=str(num)
x=list(x)[::-1]
z=int("".join(x))
print(f"output of method - 2 is {z}")

#print(type(z))
