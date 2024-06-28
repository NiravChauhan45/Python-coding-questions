"""Exercise 1: Print the sum of the current number and the previous number"""

pre_num = 0

for i in range(0,11):
    x = i + pre_num
    pre_num = i

    print(x, end=" ")