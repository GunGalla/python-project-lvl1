"""Logic module for brain-calc game."""

from random import choice, randint

from brain_games.engine import brain_games_start

RULES = 'What is the result of the expression?'
MIN_VALUE = 0
MAX_VALUE = 15
OPERATORS_LIST = ('+', '-', '*')


def brain_calc_round_generator():
    """Define number variable and answer for brain-calc.

    Returns:
        return: correct number and answer variable
    """
    first_number = randint(MIN_VALUE, MAX_VALUE)
    second_number = randint(MIN_VALUE, MAX_VALUE)
    operator = choice(OPERATORS_LIST)
    question_text = f'{first_number} {operator} {second_number}'
    operator = question_text.split()[1]
    if operator == '+':
        correct_answer = first_number + second_number
    elif operator == '-':
        correct_answer = first_number - second_number
    elif operator == '*':
        correct_answer = first_number * second_number
    else:
        print('Operation not supported!')
    return question_text, str(correct_answer)


def brain_calc_game():
    """Start and play the game."""
    brain_games_start(brain_calc_round_generator, RULES)
