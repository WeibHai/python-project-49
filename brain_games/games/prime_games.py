from prompt import string
from random import randint

def return_result(divisors):
    if len(divisors) == 2:
        return 'yes'
    else:
        return 'no'

def search_right_answer(number):
    if number == 1:
        return 'no'
    else:
        divisors = []
        divisor = number
        while divisor != 0:
            if number % divisor == 0:
                divisors.append(divisor)
                divisor -= 1
            else:
                divisor -= 1
        return return_result(divisors)


def prime():
    number = randint(1, 25)

    right_answer = search_right_answer(number)
    user_answer = string(f'Question: {number}'
                         f'\nYour answer: ')
    list_answer = [right_answer, user_answer]
    return list_answer
