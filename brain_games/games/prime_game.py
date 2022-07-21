"""Logic module for brain-prime game."""

from asking_user_prime import ask_prime
from welcome import welcome_user


def brain_prime_game():
    """Start and play the game."""
    welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    ask_prime()
