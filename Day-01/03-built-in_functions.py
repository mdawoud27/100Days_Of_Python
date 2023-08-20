#!/usr/bin/python3

# put a pic to explain
print('Welcome to Python')
abs(-27)
chr(77)
ord('d')
len('dawoud')
min(5, 6, 9, 0, 2, 10)
max(5, 6, 9, 0, 2, 10)
sum([1, 2, 3, 4, 5])

age = 21
print('I am', age, 'years old')

# Getting input from the user
name = input("What's your name? ")  # return a string
print('Hello ' + name)  # concat 2 strings

# Getting an integer from user and using int() function
name = input("What's your name? ")
yob = input('And what is your of birth? ')
age = 2023 - int(yob)  # Type cast
print('Hi ', name, 'you are ', age, ' years old')

# You can do it in one step, but it bad because you could receive a float num . Hum
number = int(input('Enter a number: '))
print(number + 10)
