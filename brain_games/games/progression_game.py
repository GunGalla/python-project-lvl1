"""Logic module for brain-progression game."""

from random import randint

from brain_games.logic.engine import brain_games_start

RULES = 'What number is missing in the progression?'


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
    hidden_number = randint(1, 9)
    progression = arithmetic_progression(randint(1, 10), randint(1, 7), 10)
    correct_answer = progression[hidden_number]
    progression[hidden_number] = '..'
    question_text = ' '.join(progression)
    return question_text, correct_answer


def brain_progression_game():
    """Start and play the game."""
    brain_games_start(brain_progress_round_generator, RULES)
