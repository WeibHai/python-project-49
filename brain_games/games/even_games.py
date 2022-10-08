from prompt import string
from random import randint


def search_right_answer(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def parity_check():
    number = randint(1, 25)

    right_answer = search_right_answer(number)
    user_answer = string(f'Question: {number}'
                         f'\nYour answer: ')
    list_answer = [right_answer, user_answer]
    return list_answer
