"""Module for greeting user."""
import prompt


def welcome_user():
    """Ask user name and greet him."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
