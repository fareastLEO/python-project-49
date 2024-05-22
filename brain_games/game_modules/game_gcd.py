#!/usr/bin/env python3

# This game is called "Calculator".
# The essence of the game is as follows: the user is shown a random mathematical
# expression, which must be calculated and the correct answer written down.

from random import randint

GAME_TASK = 'Find the greatest common divisor of given numbers.'


def game_logic():
    a = randint(1, 100)
    b = randint(1, 100)
    game_question = f'{a} {b}'

    def greatest_common_divisor(a, b):
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return str(a + b)
    game_answer = greatest_common_divisor(a, b)
    return game_question, game_answer
