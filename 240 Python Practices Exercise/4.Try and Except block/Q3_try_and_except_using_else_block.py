"""Excercise 9:using else block"""

x=int(input("enter the number: "))
y=int(input("enter the number: "))
try:
 result=x/y
except ZeroDivisionError:
 print("hey you...denominater cant be zero")
else:
 print(result)
