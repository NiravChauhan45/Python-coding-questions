countries = ("India","Australia","England","New Zeland","Pakistan","USA","South Africa","Sri lanka")
print(countries)

temp = list(countries)
temp.append("Bangladesh")
print(temp)

temp.pop(3)
print(temp)
temp[2]="West Indies"
print(tuple(temp))

countries1 = ("India","Pakistan","Afghanistan","Bangladesh","ShriLanka")
countries2 = ("USA","England","New Zeland","South Africa","West Indies")

countries = countries1 + countries2
print(countries)

tuple1 = (0,1,2,3,2,4,3,1,3,2)
res = tuple1.count(3)
print("COunt of 3 in tuple1 is : ",res)

print(tuple1.index(3,4,8))