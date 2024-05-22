import prompt

GAME_ATTEMPTS = 3  # Set the number of game attempts


def game_engine(game_module):
    print("Welcome to the Brain Games!")
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}')
    print(game_module.GAME_TASK)
    for i in range(GAME_ATTEMPTS):
        game_question, game_answer = game_module.game_logic()
        print(f'Question: {game_question}')
        user_answer = prompt.string('Your answer: ')
        user_answer = user_answer.lower().strip()
        if user_answer == game_answer:
            print('Correct!')
            continue
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{game_answer}'.")
            print(f"Let's try again, {username}!")
            return
    print(f'Congratulations, {username}!')
