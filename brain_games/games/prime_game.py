"""Logic module for brain-prime game."""

from random import randint

from brain_games.logic.engine import brain_games_start

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_VALUE = 1
MAX_VALUE = 100


def is_prime(number):
    """Define is number prime or not.

    Args:
        number: define the number need to check

    Returns:
        return: boot type answer
    """
    if number < 2:
        return False
    else:
        for num in range(2, number):
            if number % num == 0:
                return False
    return True


def brain_prime_round_generator():
    """Define number variable and answer for brain-prime.

    Returns:
        return: correct number and answer variable
    """
    number = randint(MIN_VALUE, MAX_VALUE)
    question_text = number
    if is_prime(number) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question_text, correct_answer


def brain_prime_game():
    """Start and play the game."""
    brain_games_start(brain_prime_round_generator, RULES)
