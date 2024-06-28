"""Exercise 22: Display Fibonacci series up to 10 terms"""

n1 = 0
n2 = 1

num = int(input("Enter number : "))
print(n1,end=" ")
print(n2,end=" ")

for i in range(0,num):
    n3 = n1 + n2
    n1 = n2 
    n2 = n3

    print(n3, end=" ")