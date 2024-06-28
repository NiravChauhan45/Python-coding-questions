marks = [1,2,3,"Nirav",True,None]
print(marks)

if 7 in marks:
    print("Yes")
else:
    print("No")


marks = [1,2,3,4,5,6,7,8,9]

print(marks[1:8])
print(marks[1:-1])
print(marks[1:4:2])
mark = [3,5,7]
lst = [i if i%2==0 else print("Sorry") for i in mark]
print(lst)