"""Module for brain-gcd game."""

import math
from random import randint

from question import user_question
from welcome import name


def ask_gcd():
    """Define user's answer correct or not."""
    index = 0
    while index < 3:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        number = (f'{number1} {number2}')
        user_question(number)
        answer = input('Your answer: ')
        if str(math.gcd(number1, number2)) == answer:
            print('Correct!')
            index += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. \
Correct answer was '{math.gcd(number1, number2)}'.",
            )
            print(f"Let's try again, {name}!")
            return

    if index == 3:
        print(f'Congratulations, {name}!')
