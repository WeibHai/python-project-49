from random import randint
from prompt import string


def sum_func(first_operand, second_operand):
    return first_operand + second_operand


def subtract_func(first_operand, second_operand):
    return first_operand - second_operand


def multiply_func(first_operand, second_operand):
    return first_operand * second_operand


def sort_func(focus_operator):
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


def calc():
    operators = ["+", "-", "*"]
    focus_operator = operators[randint(0, 2)]
    list_answer = sort_func(focus_operator)
    return list_answer
