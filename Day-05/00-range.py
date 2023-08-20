#!/usr/bin/python3

# Using the range() function
print(range(5))
print(type(range(5)))  # range
print(list(range(5)))

# using for loop (will be explained)
for i in range(5):  # starts with zero
    print(i)

for i in range(1, 6):  # starts with one
    print(i)

# Slicing (start, stop, step)
print(list(range(7)))  # (start = 0, stop = 7, step(default) = 1)
print(list(range(2, 7)))  # (start = 2, stop = 7, step(default) = 1)
print(list(range(2, 7, 2)))  # (start = 2, stop = 7, step = 2)
print(list(range(7, 2, -2)))  # starts with the greatest value
print(list(reversed(range(2, 7, 2))))  # reversed() function

# Using range() to make a list of numbers
nums = list(range(3, 8))
print(nums)

even_numbers = list(range(2, 15, 2))
print(even_numbers)

# Squares using loop (will be explained)
squares = []
for i in range(1, 7):
    squ = i ** 2  # pow(i, 2)
    squares.append(squ)
print(squares)

# List Comprehensions
squares = [sq ** 2 for sq in range(1, 7)]
print(squares)
