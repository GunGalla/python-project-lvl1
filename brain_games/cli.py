"""Module for greeting user."""


def welcome_user():
    """Ask username and greet him."""
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
