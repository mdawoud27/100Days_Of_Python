#!/usr/bin/python3

# format() method
name = 'dawoud'
age = 21

print('I am', name, 'and I am', age, 'years old')  # old way, man :)
# {} as replacement fields
print('I am {} and I am {} years old'.format(name, (age, 'till Oct')))  # using format()
# position arguments
print('I am {1} and I am {0} years old and my last name is {1}'.format((age, 'till Oct'), name))
# replacement fields with keyword arguments
print('mohamed is {a}, mostafa is {b}, mahmoud is {c}'.format(b=23, a=21, c=20))

# format specification
print('The value of PI is {:.3f}'.format(3.14159265))
print('we can also zero-pad integer like this {:05}'.format(3))
