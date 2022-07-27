"""Logic module for brain-gcd game."""

import math
from random import randint

from brain_games.logic.engine import brain_games_start
from brain_games.logic.rules import brain_gcd_rules


def brain_gcd_round_generator():
    """Define number variable and answer for brain-gdc.

    Returns:
        return: correct number and answer variable
    """
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    number = (f'{number1} {number2}')
    correct_answer = str(math.gcd(number1, number2))
    return number, correct_answer


def brain_gcd_game():
    """Start and play the game."""
    brain_games_start(brain_gcd_round_generator, brain_gcd_rules)
