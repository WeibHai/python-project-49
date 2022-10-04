from prompt import string
from random import randint
from sys import exit


def search(number):
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


def form_func(name_user):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count != 3:
        number = randint(1, 25)

        right_answer = search(number)
        user_answer = string(f'Question: {number}'
                             f'\nYour answer: ')
        if user_answer == right_answer:
            print("Correct!")
            count += 1
        else:
            exit(f"'{user_answer}' is wrong answer ;(."
                 f"Correct answer was '{right_answer}'."
                 f" Let's try again, {name_user}!")
    print(f'Congratulations, {name_user}!')
