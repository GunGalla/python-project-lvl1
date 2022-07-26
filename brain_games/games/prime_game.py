"""Logic module for brain-prime game."""

from brain_games.logic.engine import ask_user
from brain_games.logic.numbers import number_ans_bp
from brain_games.logic.welcome import welcome_user


def brain_prime_game():
    """Start and play the game."""
    welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    ask_user(number_ans_bp)
