#!/usr/bin/env python3
import random
from replit import clear
from art import logo


############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def init_game():
    user_cards_init = []
    computer_cards_init = []
    for _ in range(2):
        user_cards_init.append(deal_card())
        computer_cards_init.append(deal_card())
    return user_cards_init, computer_cards_init


# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.
def calculate_score(cards):
    total = sum(cards)
    if len(cards) == 2 and total == 21:
        return 0
    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
        total -= 10
    return total


def compare(user_score, computer_score):
    print(user_score, computer_score)
    if user_score == computer_score:
        print('it is a draw')
        return
    if computer_score == 21 or user_score > 21:
        print('Computer wins')
        return
    if user_score == 21 or computer_score > 21:
        print('user wins')
        return
    if computer_score > user_score:
        print('Computer wins')
        return
    else:
        print('User wins')
        return


def play_game(user_cards, computer_cards):
    print('Your cards {}, current {}'.format(user_cards, calculate_score(user_cards)))
    if calculate_score(computer_cards) == 0 or calculate_score(user_cards) > 21:
        print('Computer wins')
        return
    if input('Do you want to draw another card Y/N? ') == 'Y':
        user_cards.append(deal_card())
        play_game(user_cards, computer_cards)
    else:
        while calculate_score(computer_cards) < 17:
            computer_cards.append(deal_card())
        compare(calculate_score(user_cards), calculate_score(computer_cards))


if __name__ == '__main__':
    user_cards, computer_cards = init_game()
    play_game(user_cards, computer_cards)
    while input('Do you want to continue Y/N? ') == 'Y':
        clear()
        print(logo)
        user_cards, computer_cards = init_game()
        play_game(user_cards, computer_cards)
