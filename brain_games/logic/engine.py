"""Engine function for brain-games."""

from brain_games.logic.question import user_question
from brain_games.logic.welcome import name

ITERATIONS = 3


def ask_user(find_variables):
    """Define user's answer correct or not.

    Args:
        find_variables: defines question text and correct answer
    """
    index = 0
    while index < ITERATIONS:
        find_variables()
        variables = find_variables()
        user_question(variables[0])
        answer = input('Your answer: ')
        if variables[1] == answer:
            print('Correct!')
            index += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. \
Correct answer was '{variables[1]}'.",
            )
            print(f"Let's try again, {name}!")
            return

    if index == ITERATIONS:
        print(f'Congratulations, {name}!')
