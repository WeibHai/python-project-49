from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False
    else:
        divisors = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                divisors += 1
        return divisors == 0


def generate_round():
    number = randint(1, 25)
    game_question = (f'Question: {number}')

    right_answer = 'yes' if is_prime(number) is True else 'no'

    return right_answer, game_question
