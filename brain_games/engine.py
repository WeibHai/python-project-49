from prompt import string


ROUNDS_COUNT = 3


def distribution(game):
    print("Welcome to the Brain Games!")

    name_user = string('May I have your name? ')
    print(f'Hello, {name_user}!'
          f'\n{game.description}')
    count = 0
    while count < ROUNDS_COUNT:
        list_returned_arg = game.run_game()
        right_answer = list_returned_arg[0]
        user_answer = string(f'{list_returned_arg[1]}'
                             f'\nYour answer: ')
        if user_answer == right_answer:
            print("Correct!")
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{right_answer}'."
                  f" Let's try again, {name_user}!")
            count = 10
    else:
        if count == ROUNDS_COUNT:
            print(f'Congratulations, {name_user}!')
