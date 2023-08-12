#!/usr/bin/python3

# List is Equivalent but not equal to arrays
# Python doesn't have arrays as part of the standard types,
# but has array module in the Standard Library python array module

numbers = [21, -32, 2, 0, 12]
print(numbers)
print(type(numbers))  # list

misc = [(1, 2), 'dawoud', 27, [-23, 32]]
print(misc)
print(type(misc))  # list

# Accessing Elements in a list
names = ['mohamed', 'ali', 'mostafa', 'dawoud']
print(names[0])
print(names[-1].title())
print(names[len(names) - 1].title())  # as the same of the above
# print(names[4])  # IndexError: list index out of range
