"""Excercise 8:Write a program to print prime number 1 to 1000"""


def is_prime(num):
  for i in range(2,num):
      if num % i == 0:
          return False
  return True

for num in range(1, 1001):
    if is_prime(num):
        print(num)


