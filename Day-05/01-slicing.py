#!/usr/bin/python3

# Slicing a list => list[start : stop : step]
colors = ['red', 'yellow', 'orange', 'black', 'blue', 'white', 'green']

print(colors[0:3])  # colors[:3] start = 0, stop = 3, step = 1 by default
print(colors[2:5])  # start = 2, stop = 5, step = 1 by default
print(colors[2:])  # start = 2, stop = len(colors), step = 1 by default
print(colors[:len(colors):2])  # start = 0, stop = len(colors), step = 2
print(colors[2:-2])  # check it

print(type(colors[2:-2]))  # list
print(type(colors[0]))  # string

# Looping through a slice (loop will be explained)
# colors list
print('Here are my favourite colors:')
for color in colors[3:-1]:
    print(color.title(), end=" ")
print()

# Copying a list (tricky)
my_food = ['meat', 'rice', 'paste', 'pizza']
friend_food = my_food[:]  #
# friend_food = my_food.copy()  # as the same of the above

print('My food are:', my_food)
print('friends food are:', friend_food)

my_food.append('chicken')

print('My food are:', my_food)
print('friends food are:', friend_food)

# The following doesn't work
friend_food = my_food  # Not a copy that's the same

print('My food are:', my_food)
print('friends food are:', friend_food)

my_food.pop(3)
print('My food are:', my_food)
print('friends food are:', friend_food)
