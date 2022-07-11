#!/usr/bin/env python3
"""Script to start the brain-games."""

from brain_games.cli import welcome_user


def main():
    """Start the games."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
