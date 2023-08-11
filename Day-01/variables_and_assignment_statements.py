#!/usr/bin/python3

age = 21  # Integer Value
name = "Mohamed"  # String Value
state = True  # Boolean Value
n = -12.5  # Floating Value
m = 5 * (5.3 - 2) / 3  # operation
PI = 3.14  # Constant

# very large numbers can be more readable by underscores
num = 23_984_320

# multiple assignments
x, y, z = 1, 2, 3  # Not readable :)

#  forms of printing will explained later.. so don't worry
print(f'My name is {name}, and I am {age} years old')
print(f'Floating number: {n}\nThe result of operation: ', end=f"{m}\n")
print(f'Number = {num},  CONSTANT VALUE (PI) = {PI}')
print('x = {}, y = {}, z = {}'.format(x, y, z))
