"""Module for brain-even game."""

from random import randint

import correct_answer_be as ans
from is_even import is_number_even
from question import user_question
from welcome import name


def ask_is_even():
    """Define user's answer correct or not."""
    index = 0
    while index < 3:
        number = randint(1, 100)
        user_question(number)
        answer = input('Your answer: ')
        if (is_number_even(number) is True and answer == 'yes') or\
           (is_number_even(number) is False and answer == 'no'):
            print('Correct!')
            index += 1
        else:
            is_number_even(number)
            ans.correct_answer()
            print(
                f"'{answer}' is wrong answer ;(. \
Correct answer was '{ans.true_answer}'.",
            )
            print(f"Let's try again, {name}!")
            return

    if index == 3:
        print(f'Congratulations, {name}!')
