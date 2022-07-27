"""Logic module for brain-progression game."""

from brain_games.logic.engine import ask_user
from brain_games.logic.numbers import find_number_answer_progression
from brain_games.logic.rules import brain_progression_rules


def brain_progression_game():
    """Start and play the game."""
    ask_user(find_number_answer_progression, brain_progression_rules)
