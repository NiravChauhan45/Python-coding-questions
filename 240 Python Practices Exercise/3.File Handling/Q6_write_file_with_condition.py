"""Exercise 6: Write all content of a given file into a new file by skipping line number 5"""


# read test file
filename = "240 Python Practices Exercise/3.File and exceptions/lines.txt"
with open(filename,'r') as f:
    lines = f.readlines()
    
# open new file in write mode
with open("240 Python Practices Exercise/3.File and exceptions/new_lines.txt",'w') as f:
    count = 0
    # iterate each line from test file
    for line in lines:
        if count == 4:
            count+=1
            continue
        else:
            f.write(line)
        count+=1
