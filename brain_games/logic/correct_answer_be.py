"""Logic module for Brain-games."""

from random import randint

from is_even import is_number_even

number = randint(1, 100)


def correct_answer():
    """Define correct answer.

    Returns:
        return: variable with correct answer
    """
    if is_number_even(number) is True:
        ans = 'yes'
    else:
        ans = 'no'
    return ans


true_answer = correct_answer()
