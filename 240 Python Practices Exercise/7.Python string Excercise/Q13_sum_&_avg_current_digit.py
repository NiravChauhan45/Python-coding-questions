"""Exercise 13: Calculate the sum and average of the digits present in a string"""

str1 = "PYnative29@#8496"

str2 = list(str1)

total = 0
counter = 0
for i in str2:
    if i.isdigit() == True:
        total+=int(i)
        counter+=1

print(f"sum of digits in the given string is : {total}")
print(f"sum of digits in the given string is : {round(total/counter,2)}")