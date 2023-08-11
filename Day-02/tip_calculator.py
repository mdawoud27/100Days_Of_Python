#!/usr/bin/python3

print('Welcome to the tip calculator.')
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to giv? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_bill = tip / 100 * bill + bill
print(f'Each person should pay: ${tip_bill:0.2f}')
