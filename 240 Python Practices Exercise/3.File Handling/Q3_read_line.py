'''Excercise 3:# read line by line'''

filename = "240 Python Practices Exercise/3.File and exceptions/text_file.txt"

f = open(filename)

for line in f:
    print(line.rstrip())

print("\n\n")
with open(filename) as f_obj:
 lines=f_obj.readlines()

for line in lines:
 print(line.rstrip())