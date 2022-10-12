from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def create_progression():
    element_progression = randint(1, 10)
    step_progression = randint(2, 5)
    result = []
    while len(result) < 10:
        result.append(str(element_progression))
        element_progression = element_progression + step_progression
    return result


def generate_round():
    progression = create_progression()
    index_x_element = randint(1, 9)
    right_answer = progression[index_x_element]

    progression[index_x_element] = '..'
    progression = (' '.join(progression))

    game_question = (f'Question: {progression}')

    return str(right_answer), game_question
