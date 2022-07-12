"""Logic module for brain-games."""

print('Welcome to the Brain Games!')
name = input('May I have your name? ')


def welcome_user():
    """Ask user's name and greet him.

    Returns:
        return: user greeting
    """
    print(f'Hello, {name}!')
    return name
