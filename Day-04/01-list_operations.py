#!/usr/bin/python3

# Modifying Elements in a list
#   This is what Mutable(can be change) means
names = ['mohamed', 'ali', 'dawoud']
print(names)

names[-1] = 'mostafa'
print(names)

# Adding Elements to the end of a list
names.append('dawoud')
print(names)

# We can define empty list
fruits = []
fruits.append('apple')
fruits.append('orange')
fruits.append('banana')
fruits.append('peach')

print(fruits)
print(type(fruits))

# Concatenating lists
num1 = [1, 2, 3]
num2 = [100, 200, 300]
nums = num1 + num2

print(nums)

# Inserting Elements into a list
# `names` list
names.insert(2, 'ahmed')
names.insert(-1, 'mahmoud')
names.insert(len(names), 'abdelrahman')
print(names)

# Removing Elements from a list

#  (1) Removing an item using the del statement
# fruit list
del fruits[-1]
del fruits[1]
print(fruits)

#  (2) Removing an item using the pop() method [I can use the popped item again]
# names list
popped_name = names.pop()
print('The last popped name was', popped_name.title())
print(names)

#  (3) Popping items from any position in a list [I can use the popped item again]
# names list
first_name = names.pop(3)
print(names)
print('My grandpa name is', first_name.title())

#  (4) Removing an item by value [I can't use the popped item again]
# names list
names.remove('ahmed')
names.remove('mahmoud')
print('My name is', *names)
