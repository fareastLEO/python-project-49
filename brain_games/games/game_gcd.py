#!/usr/bin/env python3

# This game is called "Calculator".
# The essence of the game is as follows: the user is shown a random mathematical
# expression, which must be calculated and the correct answer written down.

from brain_games.engine import engine_welcome

from brain_games.engine import engine_username

from brain_games.engine import engine_test

from brain_games.engine import engine_greeting

from random import randint


def brain_gcd():
    engine_welcome()
    username = engine_username()
    print('Find the greatest common divisor of given numbers.')
    i = 0

    # The logic of how the game works is written here.
    # As a result, the 'question' and 'answer' variables should be created.
    while i < 3:
        a = randint(1, 100)
        b = randint(1, 100)
        question = f'{a} {b}'

        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a

        answer = str(a + b)
        # The end of the game logic.Variables 'username', 'question', 'answer'
        # are passed to the engine to process the result
        if engine_test(username, question, answer) is True:
            i += 1
            continue
        else:
            return

    engine_greeting(username)
