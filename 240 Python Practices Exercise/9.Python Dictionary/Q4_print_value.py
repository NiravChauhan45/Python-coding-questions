"""Exercise 4: Print the value of key 'history' from the below dict

sampleDict = { "class": { "student": { "name": "Mike", "marks": { "physics": 70, "history": 80 } } } }
expected output: 80
"""

sampleDict = { "class": { "student": { "name": "Mike", "marks": { "physics": 70, "history": 80 } } } }
print(sampleDict["class"]["student"]["marks"]["history"])
