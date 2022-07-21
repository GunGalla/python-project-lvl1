"""Logic module for brain-progression game."""

from asking_user_progression import ask_progression
from welcome import welcome_user


def brain_progression_game():
    """Start and play the game."""
    welcome_user()
    print('What number is missing in the progression?')
    ask_progression()
