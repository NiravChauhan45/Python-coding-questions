"""

Excercise 4 : now we will learn about writing to the files

passing 'w' argument to open() tells python you want to write to the file
be carefull: this will erase the contents of the file if it already exists
passing the 'a' arguement tell python you want to append to the end of an existing file

"""

filename="240 Python Practices Exercise/3.File and exceptions/programming.txt"
with open(filename,'w') as f:
 f.write("i love playing cricket as well")
