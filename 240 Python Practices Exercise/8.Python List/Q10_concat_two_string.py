"""Exercise 10: Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

expected result:
['My', 'name', 'is', 'Kelly']

"""


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

string = [i+j for i,j in zip(list1,list2)] 
print(string)