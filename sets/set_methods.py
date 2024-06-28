cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Seoul","Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Tokyo","Madrid","Delhi"}
print(cities.issuperset(cities3))
print(cities3.issubset(cities))

cities.add("Helsinki")
print(cities)
cities.remove("Helsinki")
print(cities)
cities.discard("Helsinki")
item = cities.pop()
print(item)

# print(cities)
# del cities