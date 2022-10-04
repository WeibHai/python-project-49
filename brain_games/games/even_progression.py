from prompt import string
from random import randint
from sys import exit


def create_progression():
    start_progression = randint(1, 10)
    step_progression = randint(1, 5)
    result = []
    while len(result) < 10:
        result.append(start_progression)
        start_progression += step_progression
    return result


def form_func(name_user):
    print('What number is missing in the progression?')
    count = 0
    while count != 3:
        progression = create_progression()
        prepared_progression = []
        prepared_progression.extend(progression)

        x_element = randint(2, len(progression) - 1)
        prepared_progression[x_element] = ".."

        right_answer = progression[x_element]
        user_answer = string(f'Question: {prepared_progression}'
                             f'\nYour answer: ')
        if int(user_answer) == right_answer:
            print("Correct!")
            count += 1
        else:
            exit(f"'{user_answer}' is wrong answer ;(."
                 f"Correct answer was '{right_answer}'."
                 f" Let's try again, {name_user}!")
    print(f'Congratulations, {name_user}!')
