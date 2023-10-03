#!/usr/bin/env python3

# This game is called "Parity Check".
# The essence of the game is this: the user is shown a random number.
# And he needs to answer 'yes' if the number is even, or 'no' if it’s odd.

from brain_games.engine import engine_welcome

from brain_games.engine import engine_username

from brain_games.engine import engine_test

from brain_games.engine import engine_greeting

from random import randint


def brain_even():
    engine_welcome()
    username = engine_username()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0

    # The logic of how the game works is written here.
    # As a result, the 'question' and 'answer' variables should be created.
    while i < 3:
        question = randint(1, 100)
        if (question % 2) == 0:
            answer = 'yes'
        else:
            answer = 'no'
        # The end of the game logic.Variables 'username', 'question', 'answer'
        # are passed to the engine to process the result
        if engine_test(username, question, answer) is True:
            i += 1
            continue
        else:
            return

    engine_greeting(username)
