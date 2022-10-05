from random import randint
from prompt import string


def sum_func(first_operand, second_operand):
    return first_operand + second_operand


def subtract_func(first_operand, second_operand):
    return first_operand - second_operand


def multiply_func(first_operand, second_operand):
    return first_operand * second_operand


def sort_func(focus_operator, name_user):
    first_operand = randint(10, 50)
    second_operand = randint(0, 10)
    if focus_operator == '+':
        right_answer = sum_func(first_operand, second_operand)
        user_answer = string(f'Question: {first_operand} '
                             f'+ {second_operand}\nYour answer: ')
    elif focus_operator == '-':
        right_answer = subtract_func(first_operand, second_operand)
        user_answer = string(f'Question: {first_operand} '
                             f'- {second_operand}\nYour answer: ')
    elif focus_operator == '*':
        right_answer = multiply_func(first_operand, second_operand)
        user_answer = string(f'Question: {first_operand} '
                             f'* {second_operand}\nYour answer: ')
    list_answer = [right_answer, user_answer]
    return list_answer


def calc(name_user):
    print('What is the result of the expression?')
    count = 0
    operators = ["+", "-", "*"]
    while count < 3:
        focus_operator = operators[randint(0, 2)]
        list_answer = sort_func(focus_operator, name_user)
        right_answer = list_answer[0]
        user_answer = list_answer[1]
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
                  