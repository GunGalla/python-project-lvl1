"""Module for brain-even game."""

from random import randint

from brain_games.logic.correct_answer_be import correct_answer
from brain_games.logic.question import user_question
from brain_games.logic.welcome import name


def ask_is_even():
    """Define user's answer correct or not."""
    index = 0
    while index < 3:
        number = randint(1, 100)
        user_question(number)
        answer = input('Your answer: ')
        if correct_answer(number) == answer:
            print('Correct!')
            index += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer(number)}'.",
            )
            print(f"Let's try again, {name}!")
            return

    if index == 3:
        print(f'Congratulations, {name}!')
