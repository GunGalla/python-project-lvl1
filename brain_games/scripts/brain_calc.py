#!/usr/bin/env python3
"""Script to start the brain-even game."""

from welcome import welcome_user


def main():
    """Start the game."""
    welcome_user()
    print('What is the result of the expression?')


if __name__ == '__main__':
    main()
