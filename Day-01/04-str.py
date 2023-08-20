#!/usr/bin/python3

# Really?!
# - yeah, strings are ordered sequences :)
string = 'mohamed dawoud'

print(string[0])
# Strings are Immutable sequences
# string[0] = 'm'  # TypeError: 'str' object does not support item assignment
print(string.count('m'))  # 2
print(string.index('a'))  # 3
print(dir(string))  # all methods we can use on strings
print(list(string))  # string to list
