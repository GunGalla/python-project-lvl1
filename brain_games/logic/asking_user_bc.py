"""Module for brain-calc game."""

from random import choice, randint

from question import user_question
from welcome import name

operators_list = ('+', '-', '*')


def ask_result():
    """Define user's answer correct or not."""
    index = 0
    while index < 3:
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        number = (f'{num1} {choice(operators_list)} {num2}')
        user_question(number)
        answer = input('Your answer: ')
        if eval(number) == int(answer):
            print('Correct!')
            index += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. \
Correct answer was '{eval(number)}'.",
            )
            print(f"Let's try again, {name}!")
            return

    if index == 3:
        print(f'Congratulations, {name}!')
