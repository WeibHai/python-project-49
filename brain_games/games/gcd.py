from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    first_int = randint(1, 10)
    second_int = randint(1, 10)
    game_question = (f'Question: {first_int} {second_int}')
    number = min([first_int, second_int])
    right_answer = number
    while number != 0:
        if first_int % number == 0 and second_int % number == 0:
            right_answer = number
            break
        else:
            number -= 1
    return str(right_answer), game_question
