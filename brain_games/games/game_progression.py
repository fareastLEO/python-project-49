#!/usr/bin/env python3

# This game is called "Arithmetic progression".
# The essence of the game is as follows:
# we show the player a series of numbers that forms an arithmetic
# progression by replacing any of the numbers with two dots.
# The player must determine this number.

from brain_games.engine import engine_welcome

from brain_games.engine import engine_username

from brain_games.engine import engine_test

from brain_games.engine import engine_greeting

from random import randint


def brain_progression():
    engine_welcome()
    username = engine_username()
    print('What number is missing in the progression?')
    i = 0

    while i < 3:
        # The logic of how the game works is written here.
        # As a result, the 'question' and 'answer' variables should be created.
        progression_length = randint(5, 10)
        progression_interval = randint(2, 10)
        progression_first_number = randint(1, 30)
        progression = []
        j = 0
        while j < progression_length:
            progression.append(str(progression_first_number))
            progression_first_number += progression_interval
            j += 1
        element_index = randint(0, (progression_length - 1))
        answer = str(progression[element_index])
        progression[element_index] = '..'
        question = ''
        for c in progression:
            question += c + ' '
        # The end of the game logic. Variables 'username', 'question', 'answer'
        # are passed to the engine to process the result
        if engine_test(username, question, answer) is True:
            i += 1
            continue
        else:
            return

    engine_greeting(username)
