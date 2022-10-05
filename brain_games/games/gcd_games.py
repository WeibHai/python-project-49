from prompt import string
from random import randint


def search_right_answer(first_int, second_int):
    lesser_numb = min([first_int, second_int])
    while lesser_numb != 0:
        if first_int % lesser_numb == 0 and second_int % lesser_numb == 0:
            return lesser_numb
        else:
            lesser_numb -= 1


def gcd(name_user):
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        first_int = randint(1, 10)
        second_int = randint(1, 10)
        right_answer = search_right_answer(first_int, second_int)

        user_answer = string(f'Question: {first_int} {second_int}'
                             f'\nYour answer: ')
        if int(user_answer) == right_answer:
            print("Correct!")
            count += 1
        else:
            count = 25
    else:
        if count == 3:
            print(f'Congratulations, {name_user}!')
        elif count == 25:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{right_answer}'."
                  f" Let's try again, {name_user}!")
