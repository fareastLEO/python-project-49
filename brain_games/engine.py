import prompt


def engine_welcome():
    print("Welcome to the Brain Games!")


def engine_username():
    global username
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}')
    return username


def engine_test(username, question, answer):
    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ')
    if answer == user_answer.lower():
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{answer}'.")
        print(f"Let's try again, {username}!")
        return


def engine_greeting(username):
    print(f'Congratulations, {username}!')
