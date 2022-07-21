"""Logic module for brain-gcd game."""

from asking_user_gcd import ask_gcd
from welcome import welcome_user


def brain_gcd_game():
    """Start and play the game."""
    welcome_user()
    print('Find the greatest common divisor of given numbers.')
    ask_gcd()
