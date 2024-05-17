#!/usr/bin/env python3

# This game is called "Arithmetic progression".
# The essence of the game is as follows:
# we show the player a series of numbers that forms an arithmetic
# progression by replacing any of the numbers with two dots.
# The player must determine this number.

from random import randint

GAME_TASK = 'What number is missing in the progression?'


def game_logic():
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
    game_answer = str(progression[element_index])
    progression[element_index] = '..'
    game_question = ''
    for c in progression:
        game_question += c + ' '
    return game_question, game_answer
