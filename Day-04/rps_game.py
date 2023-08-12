#!/usr/bin/python3
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (
            user_choice == 2 and computer_choice == 1):
        print('You win')
    elif computer_choice == user_choice:
        print('DRAW')
    else:
        print('You lose')





#        Another solution using math

# bot_input = randint(0, 2)
#
# # 1. Get the difference of input number for player and bot
# result = player_input - bot_input
# if result == 1 or result == -2:
#     # If you calculate all case, 1 and -2 of difference is always a win
#     result = 'YOU WIN!'
# elif result == -1 or result == 2:
#     # Inverse the cases for -1 and 2
#     result = 'YOU OPPONENT WIN'
# else:
#     # When result is 0, it's a draw (because number of input is same, no difference is produced!)
#     result = 'IT\'S A DRAW!'
