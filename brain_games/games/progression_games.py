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


def progression():
    initial_progression = create_progression()
    prepared_progression = []
    prepared_progression.extend(initial_progression)

    x_element = randint(2, len(initial_progression) - 1)
    prepared_progression[x_element] = ".."

    right_answer = initial_progression[x_element]
    user_answer = string('''Question: {} {} {} {} {} {} {} {} {} {}
Your answer: '''.format(*prepared_progression))
    list_answer = [right_answer, user_answer]
    return list_answer
