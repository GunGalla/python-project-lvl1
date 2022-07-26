"""Logic module for brain-progression game."""

from brain_games.logic.engine import ask_user
from brain_games.logic.numbers import number_ans_progression
from brain_games.logic.welcome import welcome_user


def brain_progression_game():
    """Start and play the game."""
    welcome_user()
    print('What number is missing in the progression?')
    ask_user(number_ans_progression)
