"""Excercise 20:print following pattern"""

"""

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""

n=int(input("enter the number: "))
num=1
for i in range(0,n):
   for j in range(0,i+1):
     print(num,end=" ")
     num=num+1
   print()