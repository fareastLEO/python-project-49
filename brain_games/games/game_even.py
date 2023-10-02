#!/usr/bin/env python3

# This module implements the game "Parity Check"
# For this module to work, you need to import the "username()" function
# from the "username.py" module

import prompt

from random import randint


def brain_even():
    i = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    def even_number():
        if (random_number % 2) == 0:
            return str('yes')
        return str('no')

    print('Answer "yes" if the number is even, otherwise answer "no".')
    while i < 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if even_number() == answer.lower():
            print('Correct!')
            i += 1
            continue
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{even_number()}'."
                )
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    brain_even()
