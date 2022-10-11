from random import randint


DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    first_operand = randint(0, 10)
    second_operand = randint(0, 10)

    operators = ["+", "-", "*"]
    focus_operator = operators[randint(0, 2)]

    game_question = (f'Question: {first_operand} {focus_operator}'
                     f' {second_operand}')

    if focus_operator == '+':
        right_answer = first_operand + second_operand
    elif focus_operator == '-':
        right_answer = first_operand - second_operand
    elif focus_operator == '*':
        right_answer = first_operand * second_operand
    return str(right_answer), game_question
