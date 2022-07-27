"""Logic module for brain-even game."""

from random import randint

from brain_games.logic.engine import brain_games_start
from brain_games.logic.rules import brain_even_rules


def find_number_answer_be():
    """Define number variable for brain-even.

    Returns:
        return: correct number variable
    """
    number = randint(1, 100)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer


def brain_even_game():
    """Start and play the game."""
    brain_games_start(find_number_answer_be, brain_even_rules)
