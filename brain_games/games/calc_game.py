"""Logic module for brain-calc game."""

from random import choice, randint

from brain_games.logic.engine import brain_games_start
from brain_games.logic.rules import brain_calc_rules


def find_number_answer_bc():
    """Define number variable and answer for brain-calc.

    Returns:
        return: correct number and answer variable
    """
    operators_list = ('+', '-', '*')
    number = (f'{randint(1, 10)} {choice(operators_list)} {randint(1,10)}')
    correct_answer = str(eval(number))
    return number, correct_answer


def brain_calc_game():
    """Start and play the game."""
    brain_games_start(find_number_answer_bc, brain_calc_rules)
