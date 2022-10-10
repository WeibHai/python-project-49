from random import randint


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def simplicity_test(number):
    if number == 1:
        return 'no'

    divisors = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            divisors += 1

    if divisors == 0:
        return True
    else:
        return False


def run_game():
    number = randint(1, 25)
    game_question = (f'Question: {number}')

    if simplicity_test(number) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    list_returned_arg = [right_answer, game_question]
    return list_returned_arg
