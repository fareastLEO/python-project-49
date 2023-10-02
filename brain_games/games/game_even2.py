#!/usr/bin/env python3

# This module implements the game "Parity Check"
# For this module to work, you need to import the "username()" function
# from the "username.py" module

from brain_games.engine import engine_welcome

from brain_games.engine import engine_username

from brain_games.engine import engine_test

from brain_games.engine import engine_greeting

from random import randint


def brain_even():
    engine_welcome()
    username = engine_username()
    i = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while i < 3:
        question = randint(1, 100)
        if (question % 2) == 0:
            answer = 'yes'
        else:
            answer = 'no'
        if engine_test(username, question, answer) is True:
            i += 1
            continue
        else:
            return

    engine_greeting(username)
