from random import randint


answer = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run_game():
    number = randint(1, 25)

    print(f'Question: {number}')

    if number == 1:
        return 'no'
    else:
        divisors = []
        divisor = number
        while divisor != 0:
            if number % divisor == 0:
                divisors.append(divisor)
                divisor -= 1
            else:
                divisor -= 1
        else:
            if len(divisors) == 2:
                return 'yes'
            else:
                return 'no'
