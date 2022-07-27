"""Logic module for brain-prime game."""

from brain_games.logic.engine import ask_user
from brain_games.logic.numbers import find_number_answer_bp
from brain_games.logic.rules import brain_prime_rules


def brain_prime_game():
    """Start and play the game."""
    ask_user(find_number_answer_bp, brain_prime_rules)
