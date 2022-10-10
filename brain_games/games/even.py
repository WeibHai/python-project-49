from random import randint


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_parity(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def run_game():
    number = randint(1, 25)
    game_question = (f'Question: {number}')

    right_answer = check_parity(number)

    list_returned_arg = [right_answer, game_question]
    return list_returned_arg
