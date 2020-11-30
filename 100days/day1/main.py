#!/usr/bin/env python3
import random

if __name__ == "__main__":
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

    games = [rock, paper, scissors]
    user_choice = int(input('Input your selection: 0-rock,1-paper, 2-scissors: '))
    if user_choice not in [0, 1, 2]:
        print("Invalid input")
        exit(1)

    computer_choice = random.randint(0, 2)
    print("Computer choice is {}".format(computer_choice))
    if user_choice == 0 and computer_choice == 2 or \
            user_choice == 1 and computer_choice == 0 or \
            user_choice == 2 and computer_choice == 1:
        print("User wins")
    else:
        print("Computer wins")

