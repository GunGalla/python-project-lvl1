"""Engine function for brain-games."""

from brain_games.logic.welcome import user_name, welcome_user

GAME_ROUNDS = 3


def brain_games_start(round_generator, rules):
    """Define user's answer correct or not.

    Args:
        round_generator: defines question text and correct answer
        rules: defines the current game rules
    """
    index = 0
    welcome_user()
    print(rules)
    while index < GAME_ROUNDS:
        question_text, correct_answer = round_generator()
        print(f'Question: {question_text}')
        user_answer = input('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
            index += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.",
            )
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
