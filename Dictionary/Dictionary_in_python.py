info = {
    "Nirav":"Human Being",
    "Spoon":"Object",
    45:"Rohit Sharma",
    18:"Virat Kohli",
    7:"MS Dhoni",
    "eligible":True
}

print(info["Nirav"])    
print(info.get("Nirav2"))
print(info.keys())
print(info.values())

for key,value in info.items():
    print(f"The value of corresponding to the key {key} is {value}")
