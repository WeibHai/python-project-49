from random import randint


answer = 'Answer "yes" if the number is even, otherwise answer "no".'


def run_game():
    number = randint(1, 25)

    print(f'Question: {number}')

    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
