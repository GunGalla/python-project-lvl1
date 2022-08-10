"""Logic module for brain-even game."""

from random import randint

from brain_games.logic.constants import MAX_VALUE, MIN_VALUE
from brain_games.logic.engine import brain_games_start

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even_round_generator():
    """Define number and answer variable for brain-even.

    Returns:
        return: correct number and answer variable
    """
    number = randint(MIN_VALUE, MAX_VALUE)
    question_text = number
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question_text, correct_answer


def brain_even_game():
    """Start and play the game."""
    brain_games_start(brain_even_round_generator, RULES)
