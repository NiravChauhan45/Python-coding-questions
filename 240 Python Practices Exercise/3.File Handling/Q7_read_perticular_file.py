"""Exercise 7: Read line number 4 from the following file"""


filename = "240 Python Practices Exercise/3.File and exceptions/lines.txt"

with open(filename) as f:
    lines = f.readlines()
    print(lines[3])