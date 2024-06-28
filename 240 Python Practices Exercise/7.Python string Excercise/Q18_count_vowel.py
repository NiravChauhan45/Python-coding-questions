"""Excercise 18: write progrme to count the number of vowels in the string"""

string="Milind Dattatray Mali"
vowel="AEIOUaeiou"

count = []

for i in string:
    if i in vowel:
        count.append(i)
print(" ".join(set(count)))