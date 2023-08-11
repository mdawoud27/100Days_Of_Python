#!/usr/bin/python3

# Strings and Numbers as Objects
#  - strings as objects
name = 'mohamed dawoud'
text = "  THis Is a teXT"
age = 21

print(name.title())
print(name.upper())
print(name.lower())

print(text.strip())
print(text.capitalize().strip())

msg = 'Happy ' + str(age) + ' Birthday'
print(msg)

#  - Numbers as objects
x = 127
y = 27.01
z = 2.7e5

print(bin(x))
print(x.bit_length())

print(y.as_integer_ratio())

print(z)
print(bin(int(z)))
print(int(z).bit_length())

# Using dir() function to display possible attributes
name = 'dawoud'
age = 21

print(dir(name))
print(dir(age))
