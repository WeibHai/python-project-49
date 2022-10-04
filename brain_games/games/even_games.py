from prompt import string
from random import randint
from sys import exit


def search_right_answer(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def parity_check(name_user):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        number = randint(1, 25)

        right_answer = search_right_answer(number)
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
