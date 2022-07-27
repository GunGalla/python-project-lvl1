"""Logic module for brain-calc game."""

from random import choice, randint

from brain_games.logic.engine import brain_games_start
from brain_games.logic.rules import brain_calc_rules


def brain_calc_round_generator():
    """Define number variable and answer for brain-calc.

    Returns:
        return: correct number and answer variable
    """
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    operators_list = ('+', '-', '*')
    number = (f'{number1} \
{choice(operators_list)} {number2}')
    correct_answer = str(eval(number))
    return number, correct_answer


def brain_calc_game():
    """Start and play the game."""
    brain_games_start(brain_calc_round_generator, brain_calc_rules)
