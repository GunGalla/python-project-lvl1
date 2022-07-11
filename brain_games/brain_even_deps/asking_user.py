"""Module for brain-even game"""

from random import randint
import prompt

print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')

def welcome_user():
    """Ask user name and greet him."""
    print('Hello, {0}!'.format(name))

def is_number_even(a):
    """Define is number even or not."""
    if a % 2 == 0:
        return True
    else:
        return False

def ask_is_even():
    """Function define user's answer correct or not"""
    i = 0
    while i < 3:
        number = randint(1, 100)
        question = print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')
        if is_number_even(number) == True:
            if answer == 'yes':
                print('Correct!')
                i += 1
            else:
                print("""'{0}' is wrong answer ;(. \
Correct answer was 'yes'.""".format(answer))
                print("Let's try again, {0}!".format(name))
                return
        else:
            if answer == 'no':
                print('Correct!')
                i += 1
            else:
                print("""'{0}' is wrong answer ;(. \
Correct answer was 'no'.""".format(answer))
                print("Let's try again, {0}!".format(name))
                return
    if i == 3:
        print('Congratulations, {0}!'.format(name))
