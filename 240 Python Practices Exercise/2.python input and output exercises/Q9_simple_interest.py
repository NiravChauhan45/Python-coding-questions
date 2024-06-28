"""Excercise 9: Write a program to find the simple interest when the value of principle,rate of interest
and time period is given."""

P = float(input("Principle amount : "))
R = float(input("Rate of interest : "))
T = int(input("for the time period : "))

simple_interest = P*R*T/100
print(simple_interest)

total_due=P+simple_interest
print("Total due amount will need to pay wll be ",total_due)