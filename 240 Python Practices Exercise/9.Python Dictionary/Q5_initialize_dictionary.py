"""
Exercise 5: Initialize dictionary with default values
In Python, we can initialize the keys with the same values.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

expected output: {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer',
'salary': 8000}}
"""


employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result=dict.fromkeys(employees,defaults)
print(result)
print("="*100)
print("Details of kelly: ",result["Kelly"])