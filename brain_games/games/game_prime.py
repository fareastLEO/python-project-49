#!/usr/bin/env python3

# This game is called "Is the number prime?".
# The essence of the game is as follows:
# The user is shown a random number.
# You need to answer 'yes' if the number is prime.
# Otherwise the answer is 'no'.

from brain_games.engine import engine_welcome

from brain_games.engine import engine_username

from brain_games.engine import engine_test

from brain_games.engine import engine_greeting

from random import randint


def brain_prime():  # noqa: C901
    engine_welcome()
    username = engine_username()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0

    while i < 3:
        # The logic of how the game works is written here.
        # As a result, the 'question' and 'answer' variables should be created.
        question = randint(2, 100)

        def check_prime_number(question):
            i = 2
            j = 0
            while i < question:
                if question % i == 0:
                    j += 1
                    i += 1
                    continue
                i += 1
            if j == 0:
                answer = 'yes'
                return answer
            answer = 'no'
            return answer

        answer = check_prime_number(question)
        # The end of the game logic. Variables 'username', 'question', 'answer'
        # are passed to the engine to process the result
        if engine_test(username, question, answer) is True:
            i += 1
            continue
        return

    engine_greeting(username)
