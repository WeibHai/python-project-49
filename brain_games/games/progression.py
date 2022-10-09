from random import randint


answer = 'What number is missing in the progression?'


def create_progression():
    start_progression = randint(1, 10)
    step_progression = randint(2, 5)
    result = []
    while len(result) < 10:
        result.append(start_progression)
        start_progression += step_progression
    return result


def run_game():
    initial_progression = create_progression()
    prepared_prgrsn = []
    prepared_prgrsn.extend(initial_progression)

    x_element = randint(2, len(initial_progression) - 1)
    prepared_prgrsn[x_element] = ".."

    print('Question: {} {} {} {} {} {} {} {} {} {}'.format(*prepared_prgrsn))

    return initial_progression[x_element]
