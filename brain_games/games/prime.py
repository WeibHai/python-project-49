from random import randint


answer = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run_game():
    number = randint(1, 25)
    print(f'Question: {number}')
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
