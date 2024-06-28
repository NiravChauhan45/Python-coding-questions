""""Excercise 2:read content from the file"""

filename = "240 Python Practices Exercise/3.File and exceptions/text_file.txt"

with open(filename) as f:
    content = f.readlines()
print(content)
