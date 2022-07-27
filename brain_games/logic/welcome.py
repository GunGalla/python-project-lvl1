"""Logic module for brain-games."""

print('Welcome to the Brain Games!')
user_name = input('May I have your name? ')


def welcome_user():
    """Ask user's name and greet him.

    Returns:
        return: user greeting
    """
    print(f'Hello, {user_name}!')
    return user_name
