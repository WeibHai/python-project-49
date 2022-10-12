from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = randint(1, 25)
    game_question = f'Question: {number}'

    right_answer = 'yes' if is_even(number) is True else 'no'

    return right_answer, game_question
