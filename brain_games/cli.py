"""Module for greeting user."""


def welcome_user():
    """Ask user name and greet him."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
