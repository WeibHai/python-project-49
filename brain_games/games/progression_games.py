from prompt import string
from random import randint


def create_progression():
    start_progression = randint(1, 10)
    step_progression = randint(2, 5)
    result = []
    while len(result) < 10:
        result.append(start_progression)
        start_progression += step_progression
    return result


def progression(name_user):
    print('What number is missing in the progression?')
    count = 0
    while count < 3:
        initial_progression = create_progression()
        prepared_progression = []
        prepared_progression.extend(initial_progression)

        x_element = randint(2, len(initial_progression) - 1)
        prepared_progression[x_element] = ".."

        right_answer = initial_progression[x_element]
        user_answer = string('''Question: {} {} {} {} {} {} {} {} {} {}
Your answer: '''.format(*prepared_progression))
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
