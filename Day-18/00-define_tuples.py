#!/usr/bin/python3

# Immutable list
sizes = (143, 162, 179, 200)

print(sizes[0])
print(sizes[1])
print(sizes[2])

# Trying access an item that means (Immutable)
# sizes[0] = 27  # TypeError: 'tuple' object does not support item assignment

# two dimensions
tuple_2d = ((1, 2), (3, 4), (5, 6), (7, 8))
print(tuple_2d)

# diff types in tuples
misc = (27, 'dawoud', -10, (1, 2), (3, 'mohamed'), [11, 22, 33], {0.1, 0.2, -0.3})

print(misc)
print(type(misc))

for t in misc:  # will explain later
    print(type(t))

print(misc.count(1))  # count value 1 in tuple => zero
print(misc.count(27))  # 1
print(misc.index('dawoud'))  # index of value 'dawoud'
print(misc.index((1, 2)))  # 3

# Tuple with enumerate()  // unpacking for tuples
names = ('mohamed', 'ali', 'mostafa', 'dawoud')
for idx, value in enumerate(names):
    print(idx, value)

# Writing over a tuple
# Tuple is immutable can't be changed, but I can override it with another
# names tuple
print('Original names:')
for name in names:
    print(name, end=" ")
print()
names = ('ahmed', 'gamal', 'nagy')
print('modified tuple:')
for name in names:
    print(name, end=" ")
print()

# But why modify while you have a list. use list instead :)
