"""Excercise 5: writing multiple line to empty file"""

filename = "240 Python Practices Exercise/3.File and exceptions/programming.txt"
with open(filename,'w') as f:
    f.write("self learning is awesome.\n")
    f.write("Database is set of mind\n")


with open(filename,'a+') as f:
 f.write("i love to work with data science projects \n")
 f.write("i love making the application")
 f.seek(0) # Move the pointer  to the beginning
 content = f.read()
 print(content)