"""Exercise 15: Remove empty strings from a list of strings"""

str_list = ["Nirav", "Yash", "", "Gaurav Bhai", None, "Paras Bhai", ""]

for i in str_list:
    if i == "" or i == None:
        str_list.remove(i)
print(str_list)