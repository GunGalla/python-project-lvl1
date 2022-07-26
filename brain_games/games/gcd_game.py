"""Logic module for brain-gcd game."""

from brain_games.logic.engine import ask_user
from brain_games.logic.numbers import number_ans_gcd
from brain_games.logic.welcome import welcome_user


def brain_gcd_game():
    """Start and play the game."""
    welcome_user()
    print('Find the greatest common divisor of given numbers.')
    ask_user(number_ans_gcd)
