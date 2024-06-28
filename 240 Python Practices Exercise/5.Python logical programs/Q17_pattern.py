"""Excercise 17:print following pattern"""

"""

     *
    * *
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *

"""

num = int(input("Enter number : "))
for i in range(num,0,-1):
    print(' '*i + (' *'*((num)-i)))
for i in range(num,0,-1):
    print(" "*(num-i)+" *"*i)