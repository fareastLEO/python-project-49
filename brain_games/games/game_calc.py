#!/usr/bin/env python3

# This game is called "Calculator".
# The essence of the game is as follows: the user is shown a random mathematical
# expression, which must be calculated and the correct answer written down.

from brain_games.engine import engine_welcome

from brain_games.engine import engine_username

from brain_games.engine import engine_test

from brain_games.engine import engine_greeting

from random import randint


def brain_calc():
    engine_welcome()
    username = engine_username()
    print('What is the result of the expression?')
    i = 0

    # The logic of how the game works is written here.
    # As a result, the 'question' and 'answer' variables should be created.
    while i < 3:
        operation = randint(1, 3)
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        if operation == 1:
            question = str(f'{number1} + {number2}')
            answer = str(number1 + number2)
        elif operation == 2:
            question = str(f'{number1} - {number2}')
            answer = str(number1 - number2)
        elif operation == 3:
            question = str(f'{number1} * {number2}')
            answer = str(number1 * number2)
        # The end of the game logic.Variables 'username', 'question', 'answer'
        # are passed to the engine to process the result
        if engine_test(username, question, answer) is True:
            i += 1
            continue
        else:
            return

    engine_greeting(username)
