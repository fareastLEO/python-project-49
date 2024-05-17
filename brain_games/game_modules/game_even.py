#!/usr/bin/env python3

# This game is called "Parity Check".
# The essence of the game is this: the user is shown a random number.
# And he needs to answer 'yes' if the number is even, or 'no' if it’s odd.

from random import randint

GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_logic():
    game_question = randint(1, 100)
    if (game_question % 2) == 0:
        game_answer = 'yes'
    else:
        game_answer = 'no'
    return game_question, game_answer
