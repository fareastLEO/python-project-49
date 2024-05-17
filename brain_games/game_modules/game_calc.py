#!/usr/bin/env python3

# This game is called "Calculator".
# The essence of the game is as follows: the user is shown a random mathematical
# expression, which must be calculated and the correct answer written down.

from random import randint

GAME_TASK = 'What is the result of the expression?'


def game_logic():
    operation = randint(1, 3)
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    if operation == 1:
        game_question = str(f'{number1} + {number2}')
        game_answer = str(number1 + number2)
    elif operation == 2:
        game_question = str(f'{number1} - {number2}')
        game_answer = str(number1 - number2)
    elif operation == 3:
        game_question = str(f'{number1} * {number2}')
        game_answer = str(number1 * number2)
    return game_question, game_answer
