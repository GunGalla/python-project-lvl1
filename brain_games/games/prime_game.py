"""Logic module for brain-prime game."""

from random import randint

from brain_games.logic.engine import brain_games_start

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def brain_prime_round_generator():
    """Define number variable and answer for brain-prime.

    Returns:
        return: correct number and answer variable
    """
    number = randint(1, 100)
    question_text = number
    divider = 2
    while divider ** 2 <= number and number % divider != 0:
        divider += 1
    if (divider ** 2 > number) and number != 1:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question_text, correct_answer


def brain_prime_game():
    """Start and play the game."""
    brain_games_start(brain_prime_round_generator, RULES)
