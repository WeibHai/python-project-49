from prompt import string
from random import randint


def search_right_answer(number):
    if number == 1:
        return 'no'
    else:
        separators = []
        separator = number
        while separator != 0:
            if number % separator == 0:
                separators.append(separator)
                separator -= 1
            else:
                separator -= 1
        if len(separators) == 2:
            return 'yes'
        else:
            return 'no'


def prime():
    number = randint(1, 25)

    right_answer = search_right_answer(number)
    user_answer = string(f'Question: {number}'
                         f'\nYour answer: ')
    list_answer = [right_answer, user_answer]
    return list_answer
