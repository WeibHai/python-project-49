from random import randint


answer = 'Find the greatest common divisor of given numbers.'


def run_game():
    first_int = randint(1, 10)
    second_int = randint(1, 10)
    print(f'Question: {first_int} {second_int}')
    right_answer = min([first_int, second_int])
    while right_answer != 0:
        if first_int % right_answer == 0 and second_int % right_answer == 0:
            return right_answer
        else:
            right_answer -= 1
    return right_answer
