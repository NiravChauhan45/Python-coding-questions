"""Exercise 13: Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

expected : ["Mike", "Emma", "Kelly", "Brad"]
"""


list1 = ["Mike","","Emma","Kelly","", "Brad"]
li2=[]
for i in list1:
    if i !="":
        li2.append(i)
print(li2)