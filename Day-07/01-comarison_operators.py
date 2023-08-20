#!/usr/bin/python3

print(1 == 2)  # False
print(not 1 == 2)  # True => not (statement output)
print(4 >= 2)
print(type(3 < 7))  # boolean type

# Chaining comparison operators
x = 5
print(2 <= x <= 8)  # Is x greater than or equal 2 and less than or equal 8

# 0 is False, but any other number is True
print(bool(-27))
print(bool(10.27))
print(bool(0))  # False

# Empty string is False, but any other string is True
print(bool('Hello'))
print(bool(' '))
print(bool(''))  # False

# `is` and `in` keywords
print('e' in 'hello')  # True
print('3' in [1, 2, 3])  # False --> here 3 is a char not a num

# print('mad' is 'mad')  # True
# print(27 is 27)  # True
x = 10
y = 10
print(id(x))
print(id(y))
print(x is y)  # True

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(id(l1))
print(id(l2))
print(l1 == l2)  # True  => compare the contents of two objects
print(l1 is l2)  # False => check if two objects are identical or not

# None type
# `None` in python is similar to `null` in other languages
print(type(None))  # NoneType

print(None is None)  # True
print(None is False)  # False

print(bool(None))  # False
print(bool(None) == bool(""))  # True

print(dir(None))
