"""Exercise 1: Count the occurrence of each element from a list

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
Expected Output:--> Printing count of each item {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

"""

l1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]

count = dict()

for i in l1:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)