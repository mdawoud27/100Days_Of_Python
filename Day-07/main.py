#!/usr/bim/python3
import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
# print(chosen_word)

lives = 6
end_of_game = False

from hangman_art import logo

print(logo)

# Create blanks
display = ["_" for _ in range(len(chosen_word))]

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for idx in range(len(chosen_word)):
        if chosen_word[idx] == guess:
            display[idx] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    # print(*display)

    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_art import stages

    print(stages[lives])
