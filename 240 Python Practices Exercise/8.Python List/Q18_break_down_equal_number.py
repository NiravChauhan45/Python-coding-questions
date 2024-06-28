"""Excercise 18: break down the list into equal number of chucks"""


# Method - 1

l1=[1,2,3,4,5,6,7,8,9,10,11,12]
chuck = 3
lis =[]
for i in range(0,len(l1),chuck):
    output = l1[i:i+chuck]
    lis.append(output)
print(f"Using normal for loop - {lis}")

# Method - 2

l1=[1,2,3,4,5,6,7,8,9,10,11,12]
chuck = 3
output = [l1[i:i+chuck] for i in range(0,len(l1),chuck)]
print(f"Using List Comprhension - {output}")