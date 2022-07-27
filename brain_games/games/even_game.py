"""Logic module for brain-even game."""

from brain_games.logic.engine import ask_user
from brain_games.logic.numbers import find_number_answer_be
from brain_games.logic.rules import brain_even_rules


def brain_even_game():
    """Start and play the game."""
    ask_user(find_number_answer_be, brain_even_rules)
