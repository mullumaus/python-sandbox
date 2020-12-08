#!/usr/bin/env python3
from logo import logo
from game_data import data
import random


def get_random_data():
    """

    :return:
    """
    return random.choice(data)


def check_answer(data_a, data_b):
    """

    :param guess:
    :param data_a:
    :param data_b:
    :return:
    """
    if data_a > data_b:
        return 'a'
    else:
        return 'b'


def format_data(data):
    """

    :param data:
    :return:
    """
    name = data['name']
    description = data['description']
    country = data['country']
    return f'{name}, {description} from {country}'


def start_game():
    print(logo)
    score = 0

    while True:
        data_a = get_random_data()
        data_b = get_random_data()
        if data_a == data_b:
            data_b = get_random_data()
        print(f"Compare A {format_data(data_a)}.")
        print(f"Against B {format_data(data_b)}.")

        guess = input('Who has more followers? Type A or B? ').lower()
        result = check_answer(data_a['follower_count'], data_b['follower_count'])
        if guess == result:
            score += 1
            print('You are right, current score {}'.format(score))
        else:
            print('Sorry, that is wrong, final score: {}'.format(score))
            break


if __name__ == "__main__":
    start_game()

