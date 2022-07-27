"""Logic module for brain-even game."""

from random import randint

from brain_games.logic.engine import brain_games_start
from brain_games.logic.rules import brain_even_rules


def brain_even_round_generator():
    """Define number and answer variable for brain-even.

    Returns:
        return: correct number and answer variable
    """
    number = randint(1, 100)
    question_text = number
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question_text, correct_answer


def brain_even_game():
    """Start and play the game."""
    brain_games_start(brain_even_round_generator, brain_even_rules)
