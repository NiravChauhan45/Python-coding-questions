"""Exercise 4: Create a new list from a two list using the following condition. Given a two list of
numbers, write a program to create a new list such that the new list should contain odd numbers
from the first list and even numbers from the second list."""


l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l3=[]

for i in l1:
    if i%2!=0:
        l3.append(i)
for i in l2:
    if i%2==0:
        l3.append(i)

print(l3)
