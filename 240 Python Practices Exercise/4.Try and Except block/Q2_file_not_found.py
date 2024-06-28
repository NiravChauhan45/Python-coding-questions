"""Excercise 2: Handle error if file is not found in current directory"""

filename="gautam.txt"
try:
  with open(filename) as f:
     content=f.read()
  print(content)
except FileNotFoundError:
  print(f"Dear user {filename} may be this file dont exist in directory!")