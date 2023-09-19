import random
import sys
import game_data
import art


def generate_account():
    """Get data from random account"""
    return random.choice(game_data.data)

def formate_player_account(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}."

def get_followers(account):
    """Returns the followers of account."""
    return account["follower_count"]

def check_followers(account_a, account_b):
    """Compare between accounts followers

    Return:
        Account that has bigger number of followers.
    """
    if get_followers(account_a) > get_followers(account_b):
        return account_a
    else:
        return account_b

def check_answer(guess, a_followers, b_followers):
    """Checks who has many followers"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():

    score = 0
    account_temp = generate_account()
    # account_b = generate_account()
    is_game_over = False

    while not is_game_over:

        print(art.logo)

        account_a = account_temp
        account_b = generate_account()

        if account_a == account_b:
            account_b = generate_account()

        print(f"Compare A: {formate_player_account(account_a)}")
        # print(get_followers(account_a))

        print(art.vs)

        print(f"Against B: {formate_player_account(account_b)}")
        # print(get_followers(account_b))

        guess = input("Who has more followers? Type 'A' or 'B': ").lower().strip()
        is_correct = check_answer(guess, get_followers(account_a), get_followers(account_b))

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            account_temp = check_followers(account_a, account_b)
            sys.stdout.write('\033c')
            sys.stdout.flush()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            is_game_over = True


game()