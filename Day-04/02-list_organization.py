#!/usr/bin/python3

# Sorting a list permanently with the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
print(cars)

cars.sort(reverse=True)  # sorting in reverse order
print(cars)

# Sorting a list temporarily with the sorted() function
names = ['mohamed', 'ali', 'mostafa', 'dawoud']

print('Here is the original list:\n\t', names)
print('Here is the sorted list:\n\t', sorted(names))
print('Here is the original list again:\n\t', names)  # And u can use another temp list

# Printing a list in reverses order
fruits = ['banana', 'peach', 'apple', 'orange']
fruits.reverse()  # Not sorted, just reverse it
print(fruits)

# Finding the length of a list
print(f'The length of names list is: {len(names)}')

# list() constractor function
# convert some values to list
print(list([1, 2, 3, 4]))
print(list('mohamed'))
print(type(list('mad')))  # list

# list() with enumerate()
# names list
print(list(enumerate(names)))  # unpacking sequences

# using enumerate() with for loop(will be explained)
for index, value in enumerate(names):
    print(index, value)

# Avoiding index error when working with lists
# fruit list contains 3 indexes and 4 values
print(fruits[4])  # IndexError: list index out of range

empty_list = []
print(len(empty_list))  # zero
print(empty_list[-1])  # IndexError: list index out of range
