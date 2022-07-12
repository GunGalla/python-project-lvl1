#!/usr/bin/env python3
"""Script to start the brain-even game."""

import asking_user as ask


def main():
    """Start the game."""
    ask.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    ask.ask_is_even()


if __name__ == '__main__':
    main()
