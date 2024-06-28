"""Excercise 6: Print all the armstrong numbers in the range of 100 to 1000"""

armstrong_list = []

for i in range(100,1000):
    a = i % 10   
    x = i // 10
    b = x % 10
    c = x // 10

    if (a**3) + (b**3) + (c**3) == i:
        armstrong_list.append(i)
print(armstrong_list)