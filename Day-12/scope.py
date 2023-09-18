#!/usr/bin/python3

# Scope

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}") # 2

increase_enemies()
print(f"enemies outside function: {enemies}") # 1

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength) # NameError: name 'potion_strength' is not defined

# Global Scope

player_health = 10

def game():
    def drink():
        potion_strength = 2 # local variable 
        print(player_health) # 10 cuz it is a global variable

    drink()

game()

# Global Constant

PI = 3.14159
CODEGORCES_HANDLE = "dawoud27"