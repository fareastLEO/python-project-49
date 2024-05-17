#!/usr/bin/env python3

# This game is called "Is the number prime?".
# The essence of the game is as follows:
# The user is shown a random number.
# You need to answer 'yes' if the number is prime.
# Otherwise the answer is 'no'.

from random import randint

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_logic():
    game_question = randint(2, 100)
    i = 2
    j = 0
    while i < game_question:
        if game_question % i == 0:
            j += 1
            i += 1
            continue
        i += 1
    if j == 0:
        game_answer = 'yes'
    else:
        game_answer = 'no'
    return game_question, game_answer
