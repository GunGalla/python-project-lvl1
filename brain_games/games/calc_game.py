"""Logic module for brain-calc game."""

from brain_games.logic.asking_user_bc import ask_result
from brain_games.logic.welcome import welcome_user


def brain_calc_game():
    """Start and play the game."""
    welcome_user()
    print('What is the result of the expression?')
    ask_result()
