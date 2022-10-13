from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def is_gcd(first_int, second_int, number):
    while number != 0:
        if first_int % number == 0 and second_int % number == 0:
            return number
            break
        else:
            number -= 1


def generate_round():
    first_int = randint(1, 10)
    second_int = randint(1, 10)
    game_question = (f'Question: {first_int} {second_int}')

    number = min([first_int, second_int])

    right_answer = is_gcd(first_int, second_int, number)
    return str(right_answer), game_question
