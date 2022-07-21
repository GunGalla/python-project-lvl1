"""Logic module for brain-even game."""

from brain_games.logic.asking_user_be import ask_is_even
from brain_games.logic.welcome import welcome_user


def brain_even_game():
    """Start and play the game."""
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    ask_is_even()
