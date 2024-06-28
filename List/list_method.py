l = [1,2,3,4]
print(l)

l.append(45)
print(l)

l.sort(reverse=True)
print(l) 

l.reverse()
print(l)

l = [18,45,12,45,3,17,333]
print(l.count(45))

m = l.copy()
print(m)
m[0] = 7
print(m)

l.insert(0,18)
print(l)
m = [900,1000,200]
l.extend(m)
print(l+m)
print(l)