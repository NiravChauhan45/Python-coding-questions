"""Excercise 20:print following pattern"""

"""

*
**
***
****
*****
****
***
**
*

"""


num = int(input("Enter number : "))

for i in range(1,num):
    print("*"*i,end=" ")
    print()
for i in range(num,0,-1):
    print("*"*i)

