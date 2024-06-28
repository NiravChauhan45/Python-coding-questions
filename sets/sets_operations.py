s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2)
# print(s1,s2)

cities1 = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid","Mumbai"}
cities3 = cities1.intersection(cities2)

cities3.intersection_update(cities2)
# print(cities3)


print(cities1.symmetric_difference(cities2)) #symmetric_difference = union - intersection

print(cities1.difference(cities2)) # diffrence = cities1 - cities2


set1 = {2,4,6}
set2 = {2,4,6,8}
set1.symmetric_difference_update(set2)
print(set1)
