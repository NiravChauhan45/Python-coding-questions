"""
Exercise 10: Check if all items in the tuple are the same
tuple1 = (45, 45, 45, 45)
"""

tuple1 = (45, 45, 45, 45)

for i in tuple1:
    if i == tuple1[0]:
        print("yes all the item are same in the given tuple")
        break
    else:
        print("No all the item are not same in the given table")