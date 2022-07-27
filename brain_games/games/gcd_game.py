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
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    number = (f'{first_number} {second_number}')
    correct_answer = str(math.gcd(first_number, second_number))
    return number, correct_answer


def brain_gcd_game():
    """Start and play the game."""
    brain_games_start(brain_gcd_round_generator, brain_gcd_rules)
