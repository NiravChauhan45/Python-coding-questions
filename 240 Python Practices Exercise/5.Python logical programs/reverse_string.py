name = "my name is nirav"
n = name.split()
print(n)
l = []
for i in n:
    l.append(i[::-1])
print(l)