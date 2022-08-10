"""Logic module for brain-gcd game."""

import math
from random import randint

from brain_games.logic.engine import brain_games_start

RULES = 'Find the greatest common divisor of given numbers.'


def brain_gcd_round_generator():
    """Define number variable and answer for brain-gdc.

    Returns:
        return: correct number and answer variable
    """
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    question_text = (f'{first_number} {second_number}')
    correct_answer = str(math.gcd(first_number, second_number))
    return question_text, correct_answer


def brain_gcd_game():
    """Start and play the game."""
    brain_games_start(brain_gcd_round_generator, RULES)
