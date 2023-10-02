#!/usr/bin/env python3

from brain_games.engine import engine_welcome

from brain_games.engine import engine_username

from brain_games.engine import engine_test

from brain_games.engine import engine_greeting

from random import randint


def brain_calc():
    engine_welcome()
    username = engine_username()
    i = 0
    print('What is the result of the expression?')

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
        if engine_test(username, question, answer) is True:
            i += 1
            continue
        else:
            return

    engine_greeting(username)
