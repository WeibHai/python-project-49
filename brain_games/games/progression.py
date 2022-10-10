from random import randint


description = 'What number is missing in the progression?'


def create_progression():
    element_progression = randint(1, 10)
    step_progression = randint(2, 5)
    result = []
    while len(result) < 10:
        result.append(element_progression)
        element_progression += step_progression
    return result


def run_game():
    progression = create_progression()
    right_answer = progression[randint(1, 9)]

    progression[progression.index(right_answer)] = '..'

    progression = (' '.join(list(map(str, progression))))

    game_question = (f'Question: {progression}')

    list_returned_arg = [str(right_answer), game_question]
    return list_returned_arg
