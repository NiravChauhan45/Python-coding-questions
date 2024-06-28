"""
Exercise 6: Create a dictionary by extracting the keys from a given dictionary
Write a Python program to create a new dictionary by extracting the mentioned keys from the below
dictionary.

sample_dict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
key to extract keys = ["name", "salary"]

expected output:
{'name': 'Kelly', 'salary': 8000}
"""

sample_dict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

keys = ["name","salary"]

result = {}

for k in keys:
    result.update({k:sample_dict[k]})
print(result)
