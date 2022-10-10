from random import randint


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def simplicity_test(number):
    if number == 1:
        return 'no'
    divisors = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            divisors = divisors + 1
    if divisors == 0:
        return 'yes'
    else:
        return 'no'


def run_game():
    number = randint(1, 25)
    game_question = (f'Question: {number}')

    right_answer = simplicity_test(number)

    list_returned_arg = [right_answer, game_question]
    return list_returned_arg
