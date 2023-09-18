#!/usr/bin/python3
from random import randint


EASY_LEVEL = 10
HARD_LEVEL = 5

def set_range(a = 1, b = 100):
    return randint(a, b)

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_number(answer, guess, turns):
    """Checks answer against guess.

    Return:
        The number of turns remaining."""
    if answer > guess:
        if answer - guess <= 5:
            print("You so close.")
            return turns - 1
        else:
            print("Too low.")
            return turns - 1
    elif answer < guess:
        if guess - answer <= 5:
            print("You so close.")
            return turns - 1
        else:
            print("Too high.")
            return turns - 1
    else:
        print(f"You get it, the correct answer is {answer}")

def game():

    print("Welcome to the Number Guessing Game!")
    choose = input("I'm thinking of a number between 1 and 100 click 'c' .\nIf you can reset the range just click 'r' ")

    if choose == "c":
        answer = set_range(a=1, b=100)
    elif choose == "r":
        a = int(input("Enter the first range: "))
        b = int(input("Enter the second range: "))
        answer = set_range(a, b)
    # print(answer)

    turns = set_difficulty()

    guess = -1
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_number(answer, guess, turns)

        if turns == 0:
            print("You have run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
