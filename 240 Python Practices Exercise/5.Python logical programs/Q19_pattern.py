"""Excercise 19:print following pattern"""

"""

1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6

"""


num = int(input("ENter number : "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()