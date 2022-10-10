from random import randint


description = 'What is the result of the expression?'


def run_game():
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
    list_returned_arg = [str(right_answer), game_question]
    return list_returned_arg
