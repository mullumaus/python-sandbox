#!/usr/bin/env python3

from art import logo
from random import randint

def select_difficulty():
    level = input("please choose a difficulty, type 'easy' or 'hard': ")
    if level == 'hard':
        return 5
    else:
        return 10


def check_answer(guess, answer, turns):
    """

    :param guess:
    :param answer:
    :param turns:
    :return:
    """
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
    else:
        print('You got it!')
    return turns - 1


def game():
    print(logo)
    print("welcome to number guess game")
    answer = randint(1, 100)
    turns = select_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose. correct answer is {}".format(answer))
            return
        elif guess != answer:
            print("Guess again")


if __name__ == '__main__':
    game()



