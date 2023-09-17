#!/usr/bin/python3
import sys


def find_highest_bidder(bidding_record):
    """Function that prints the highest bidder

    Args:
        bidding_record(dict)
    """
    if bidding_record:
        winner = ""
        highest_amout = 0
        for bigger in bidding_record:
            if highest_amout < bidding_record[bigger]:
                highest_amout = bidding_record[bigger]
                winner = bigger
        print(f"The winner is {winner} with ${highest_amout} bid.")
    else:
        print("NO bids entered.")


bid_dict = {}
user_flag = True

while user_flag:
    name = input("What is your name? ")
    bid = float(input("What is your bid price? $"))

    bid_dict[name] = bid
    another_user = input("Is there another user? (Yes/ No) ").lower()
    if another_user == "yes" or another_user == "y":
        user_flag = True
        sys.stdout.write("\033c")
        sys.stdout.flush()
    elif another_user == "no" or another_user == 'n':
        find_highest_bidder(bid_dict)
        user_flag = False
    else:
        print("Fucked up man, enter a valid option!")
