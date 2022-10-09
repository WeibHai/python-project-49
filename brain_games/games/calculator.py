from random import randint


answer = 'What is the result of the expression?'


def run_game():
    first_operand = randint(0, 10)
    second_operand = randint(0, 10)

    operators = ["+", "-", "*"]
    focus_operator = operators[randint(0, 2)]

    print(f'Question: {first_operand} {focus_operator} {second_operand}')

    if focus_operator == '+':
        right_answer = first_operand + second_operand
    elif focus_operator == '-':
        right_answer = first_operand - second_operand
    elif focus_operator == '*':
        right_answer = first_operand * second_operand
    return right_answer
