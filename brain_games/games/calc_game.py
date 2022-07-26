"""Logic module for brain-calc game."""

from brain_games.logic.engine import ask_user
from brain_games.logic.numbers import find_number_answer_bc
from brain_games.logic.welcome import welcome_user


def brain_calc_game():
    """Start and play the game."""
    welcome_user()
    print('What is the result of the expression?')
    ask_user(find_number_answer_bc)
