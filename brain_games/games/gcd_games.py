from prompt import string
from random import randint


def search_right_answer(first_int, second_int):
    lesser_numb = min([first_int, second_int])
    while lesser_numb != 0:
        if first_int % lesser_numb == 0 and second_int % lesser_numb == 0:
            return lesser_numb
        else:
            lesser_numb -= 1


def gcd():
    first_int = randint(1, 10)
    second_int = randint(1, 10)
    right_answer = search_right_answer(first_int, second_int)
    user_answer = string(f'Question: {first_int} {second_int}'
                         f'\nYour answer: ')
    list_answer = [right_answer, user_answer]
    return list_answer
