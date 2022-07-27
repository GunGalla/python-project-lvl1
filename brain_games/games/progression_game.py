"""Logic module for brain-progression game."""

from random import randint

from brain_games.logic.engine import brain_games_start
from brain_games.logic.rules import brain_progression_rules


def arithmetic_progression(start, step, iterations):
    """Create an arithmetic progression.

    Args:
        start: first number of progression
        step: difference between elements
        iterations: amount of elements

    Returns:
        return: arithmetic progression
    """
    first_num = start
    final = ''
    for num in range(1, iterations + 1):
        final += (str(first_num) + ' ')
        first_num += step
    return final.split()


def find_number_answer_progression():
    """Define number variable and answer for brain-progression.

    Returns:
        return: correct number and answer variable
    """
    hidden_number = randint(1, 9)
    solution = arithmetic_progression(randint(1, 10), randint(1, 7), 10)
    correct_answer = solution[hidden_number]
    solution[hidden_number] = '..'
    number = ' '.join(solution)
    return number, correct_answer


def brain_progression_game():
    """Start and play the game."""
    brain_games_start(find_number_answer_progression, brain_progression_rules)
