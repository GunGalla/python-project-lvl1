"""Logic module for brain-gcd game."""

from brain_games.logic.engine import ask_user
from brain_games.logic.numbers import find_number_answer_gcd
from brain_games.logic.rules import brain_gcd_rules


def brain_gcd_game():
    """Start and play the game."""
    ask_user(find_number_answer_gcd, brain_gcd_rules)
