"""Exercise 11: Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Expected result:
['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

"""

list1 = ["Hello","take"]
list2 = ["Dear","sir"]

for i in list1:
    for j in list2:
        print(i+" "+j)

# using list comprehension

print([i+" "+j for i in list1 for j in list2])