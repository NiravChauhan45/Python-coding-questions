"""Excercise 6 :Count the frequency of a particular character in a provided string. Eg 'hello how are you'
is the string, the frequency of h in this string is 2."""

txt = input("Enter text : ")
char = input("Enter the character : ") 

count = 0
for i in txt:
    if i in char:
        count+=1
print(f"frequency of searched character is {count} times")
        
