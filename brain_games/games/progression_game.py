"""Logic module for brain-progression game."""

from random import randint

from brain_games.logic.engine import brain_games_start
from brain_games.logic.rules import brain_progress_rules


def arithmetic_progression(start, step, iterats):
    """Create an arithmetic progression.

    Args:
        start: first number of progress
        step: difference between elements
        iterats: amount of elements

    Returns:
        return: arithmetic progress
    """
    first_num = start
    final = ''
    for num in range(1, iterats + 1):
        final += (str(first_num) + ' ')
        first_num += step
    return final.split()


def brain_progress_round_generator():
    """Define number variable and answer for brain-progress.

    Returns:
        return: correct number and answer variable
    """
    progress_start = randint(1, 10)
    progress_step = randint(1, 7)
    number_of_elements = 10
    hidden_number = randint(1, 9)
    progress = arithmetic_progression(
        progress_start, progress_step, number_of_elements,
    )
    correct_answer = progress[hidden_number]
    progress[hidden_number] = '..'
    number = ' '.join(progress)
    return number, correct_answer


def brain_progression_game():
    """Start and play the game."""
    brain_games_start(brain_progress_round_generator, brain_progress_rules)
