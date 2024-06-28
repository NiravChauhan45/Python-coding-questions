"""Excercise 18:print following pattern"""

"""

1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6

"""


num = int(input("ENter number : "))
for i in range(1,num+1):
    for j in range(0,i):
        print(i,end=" ")
    print()