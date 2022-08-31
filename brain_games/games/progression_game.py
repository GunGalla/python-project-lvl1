"""Logic module for brain-progression game."""

from random import randint

from brain_games.engine import brain_games_start

RULES = 'What number is missing in the progression?'
MIN_VALUE = 1
MAX_VALUE = 10
PROGRESSION_ITERATIONS = 10
MIN_HIDDEN_NUM_POSITION = 1
MAX_HIDDEN_NUM_POSITION = 9


def arithmetic_progression(start, step, iterations):
    """Create an arithmetic progression.

    Args:
        start: first number of progress
        step: difference between elements
        iterations: amount of elements

    Returns:
        return: arithmetic progress
    """
    first_num = start
    final = ''
    for num in range(1, iterations + 1):
        final += (str(first_num) + ' ')
        first_num += step
    return final.split()


def brain_progress_round_generator():
    """Define number variable and answer for brain-progress.

    Returns:
        return: correct number and answer variable
    """
    hidden_number = randint(
        MIN_HIDDEN_NUM_POSITION, MAX_HIDDEN_NUM_POSITION,
    )
    progression = arithmetic_progression(
        randint(MIN_VALUE, MAX_VALUE),
        randint(MIN_VALUE, MAX_VALUE), PROGRESSION_ITERATIONS,
    )
    correct_answer = progression[hidden_number]
    progression[hidden_number] = '..'
    question_text = ' '.join(progression)
    return question_text, correct_answer


def brain_progression_game():
    """Start and play the game."""
    brain_games_start(brain_progress_round_generator, RULES)
