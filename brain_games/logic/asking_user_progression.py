"""Module for brain-progression game."""

from random import randint

from progression import ar_progression
from question import user_question
from welcome import name


def ask_progression():
    """Define user's answer correct or not."""
    index = 0
    while index < 3:
        hidden_number = randint(1, 9)
        solution = ar_progression(randint(1, 10), randint(1, 7), 10)
        correct_answer = solution[hidden_number]
        solution[hidden_number] = '..'
        user_question(' '.join(solution))
        answer = input('Your answer: ')
        if str(correct_answer) == answer:
            print('Correct!')
            index += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.",
            )
            print(f"Let's try again, {name}!")
            return

    if index == 3:
        print(f'Congratulations, {name}!')
