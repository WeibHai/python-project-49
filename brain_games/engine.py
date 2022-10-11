from prompt import string


ROUNDS_COUNT = 3


def run(game):
    print("Welcome to the Brain Games!")

    name_user = string('May I have your name? ')
    print(f'Hello, {name_user}!'
          f'\n{game.DESCRIPTION}')
    count = 0
    while count < ROUNDS_COUNT:
        right_answer, question = game.generate_round()
        user_answer = string(f'{question}'
                             f'\nYour answer: ')
        if user_answer == right_answer:
            print("Correct!")
            count += 1
        else:
            return print(f"'{user_answer}' is wrong answer ;(."
                         f"Correct answer was '{right_answer}'."
                         f" Let's try again, {name_user}!")
    print(f'Congratulations, {name_user}!')
