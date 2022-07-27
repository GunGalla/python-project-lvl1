"""Logic module for brain-prime game."""

from random import randint

from brain_games.logic.engine import brain_games_start
from brain_games.logic.rules import brain_prime_rules


def find_number_answer_bp():
    """Define number variable and answer for brain-prime.

    Returns:
        return: correct number and answer variable
    """
    number = randint(1, 100)
    divider = 2
    while divider ** 2 <= number and number % divider != 0:
        divider += 1
    if (divider ** 2 > number) or number == 1:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer


def brain_prime_game():
    """Start and play the game."""
    brain_games_start(find_number_answer_bp, brain_prime_rules)
