"""Exercise 2: Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
"""

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = zip(keys,values)

result = dict(my_dict)
print(result)