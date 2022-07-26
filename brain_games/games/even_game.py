"""Logic module for brain-even game."""

from brain_games.logic.engine import ask_user
from brain_games.logic.numbers import find_number_answer_be
from brain_games.logic.welcome import welcome_user


def brain_even_game():
    """Start and play the game."""
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    ask_user(find_number_answer_be)
