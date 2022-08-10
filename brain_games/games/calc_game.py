"""Logic module for brain-calc game."""

from random import choice, randint

from brain_games.logic.engine import brain_games_start

RULES = 'What is the result of the expression?'


def brain_calc_round_generator():
    """Define number variable and answer for brain-calc.

    Returns:
        return: correct number and answer variable
    """
    first_number = randint(1, 10)
    second_number = randint(1, 10)
    operators_list = ('+', '-', '*')
    question_text = (f'{first_number} \
{choice(operators_list)} {second_number}')
    operator = question_text.split()[1]
    if operator == '+':
        correct_answer = first_number + second_number
    elif operator == '-':
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number
    return question_text, str(correct_answer)


def brain_calc_game():
    """Start and play the game."""
    brain_games_start(brain_calc_round_generator, RULES)
