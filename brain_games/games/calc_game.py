"""Logic module for brain-calc game."""

from random import choice, randint

from brain_games.logic.engine import brain_games_start
from brain_games.logic.rules import brain_calc_rules


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
    correct_answer = str(eval(question_text))
    return question_text, correct_answer


def brain_calc_game():
    """Start and play the game."""
    brain_games_start(brain_calc_round_generator, brain_calc_rules)
