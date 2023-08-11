#!/usr/bin/python3

# Pizza Order Challenge
print("Welcome to Python Pizza Deliveries!")
menu = 'This is our Menu for today!\n- Small Pizza: $15\n- Medium Pizza: $20\n- Large Pizza: $25'
print(menu)
size = input ("What's size pizza do you want? S, M, or L: ")
price = 0
if size == 'S' or 's':
    print('Nice!')
    price = 15
elif size == 'M' or 'm':
    print('Good choice!')
    price = 20
elif size == 'M' or 'm':
    print('Cool!')
    price = 25

pepperoni = 'Pepperoni for Small Pizza: +$2\nPepperoni for Medium or Large Pizza: +$3'
print(pepperoni)
add_pepperoni = input("Do you want pepperoni? Y or N: ")
if add_pepperoni == 'y' or 'Y':
    print('You added pepperoni!')
    if size == 's' or 'S':
        price += 2
    else:
        price += 3
else:
    print('OK, you don\'t want')

cheese = 'Extra cheese for any size pizza: +$1'
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == 'Y' or 'y':
    print('Oooh, You added cheese to your perfect pizza!')
    price += 1

print(f'Your final bill is: ${price}')
