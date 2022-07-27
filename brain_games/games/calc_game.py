"""Logic module for brain-calc game."""

from brain_games.logic.engine import ask_user
from brain_games.logic.numbers import find_number_answer_bc
from brain_games.logic.rules import brain_calc_rules


def brain_calc_game():
    """Start and play the game."""
    ask_user(find_number_answer_bc, brain_calc_rules)
