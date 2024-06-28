"""Excercise 7: Take a number from the user and find the number of digits in it."""

n = input("Enter number : ")
digit_list = list(str(n))

count=0
for i in digit_list:
    count+=1
print(count)
