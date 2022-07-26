"""Number and answer variables for brain-games."""

import math
from random import choice, randint

from brain_games.logic.progression import ar_progression


def number_ans_be():
    """Define number variable for brain-even.

    Returns:
        return: correct number variable
    """
    number = randint(1, 100)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer


def number_ans_bc():
    """Define number variable and answer for brain-calc.

    Returns:
        return: correct number and answer variable
    """
    operators_list = ('+', '-', '*')
    number = (f'{randint(1, 10)} {choice(operators_list)} {randint(1,10)}')
    correct_answer = str(eval(number))
    return number, correct_answer


def number_ans_gcd():
    """Define number variable and answer for brain-gdc.

    Returns:
        return: correct number and answer variable
    """
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    number = (f'{number1} {number2}')
    correct_answer = str(math.gcd(number1, number2))
    return number, correct_answer


def number_ans_progression():
    """Define number variable and answer for brain-progression.

    Returns:
        return: correct number and answer variable
    """
    hidden_number = randint(1, 9)
    solution = ar_progression(randint(1, 10), randint(1, 7), 10)
    correct_answer = solution[hidden_number]
    solution[hidden_number] = '..'
    number = ' '.join(solution)
    return number, correct_answer


def number_ans_bp():
    """Define number variable and answer for brain-prime.

    Returns:
        return: correct number and answer variable
    """
    number = randint(1, 100)
    divider = 2
    while divider ** 2 <= number and number % divider != 0:
        divider += 1
    if (divider ** 2 > number) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
