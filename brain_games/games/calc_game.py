"""Logic module for brain-calc game."""

from asking_user_bc import ask_result
from welcome import welcome_user


def brain_calc_game():
    """Start and play the game."""
    welcome_user()
    print('What is the result of the expression?')
    ask_result()
