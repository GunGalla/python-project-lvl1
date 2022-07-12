"""Module for brain-even game."""
from random import randint

import prompt

print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')


def welcome_user():
    """Ask user name and greet him."""
    print('Hello, {0}!'.format(name))


def is_number_even(num):
    """Find is number even or not.

    Args:
        num: number to check

    Returns:
        result: is number even or not in bool format.
    """
    return num % 2 == 0


def ask_is_even():
    """Define user's answer correct or not."""
    index = 0
    while index < 3:
        number = randint(1, 100)
        print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')
        if is_number_even(number) is True:
            if answer == 'yes':
                print('Correct!')
                index += 1
            else:
                print(
                    "'{0}' is wrong answer ;(. \
Correct answer was 'yes'.".format(answer),
                )
                print("Let's try again, {0}!".format(name))
                return
        else:
            if answer == 'no':
                print('Correct!')
                index += 1
            else:
                print(
                    "'{0}' is wrong answer ;(. \
Correct answer was 'no'.".format(answer),
                )
                print("Let's try again, {0}!".format(name))
                return
    if index == 3:
        print('Congratulations, {0}!'.format(name))
