"""Logic module for brain-even game."""

from asking_user_bc import ask_sum
from welcome import welcome_user


def brain_even_game():
    """Start and play the game."""
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    ask_sum()
