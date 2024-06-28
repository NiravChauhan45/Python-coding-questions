"""Exercise 10: Count all letters, digits, and special symbols from a given string

given-->str1 = "P@#yn26at^&i5ve"
expected-->Total counts of chars, digits, and symbols
"""

str1 = "P@#yn26at^&i5ve"
l1 = list(str1)

char = 0
digit = 0
special_char = 0

for i in l1:
    if i.isalpha() == True:
        char+=1
    elif i.isdigit() == True:
        digit+=1
    else:
        special_char+=1

print(f"Char : {char}")
print(f"Digit : {digit}")
print(f"special_char : {special_char}")