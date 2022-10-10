from random import randint


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_parity(number):
    if number % 2 == 0:
        return True
    else:
        return False


def run_game():
    number = randint(1, 25)
    game_question = (f'Question: {number}')

    if check_parity(number) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    list_returned_arg = [right_answer, game_question]
    return list_returned_arg
