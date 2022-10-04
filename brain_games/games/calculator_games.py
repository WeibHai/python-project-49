from random import randint
from prompt import string
from sys import exit


def sum_func(first_operand, second_operand, name_user):
    right_answer = first_operand + second_operand
    user_answer = string(f'Question: {first_operand} '
                         f'+ {second_operand}\nYour answer: ')
    if int(user_answer) == right_answer:
        print("Correct!")
    else:
        exit(f"'{user_answer}' is wrong answer ;(."
             f"Correct answer was '{right_answer}'."
             f" Let's try again, {name_user}!")


def subtract_func(first_operand, second_operand, name_user):
    right_answer = first_operand - second_operand
    user_answer = string(f'Question: {first_operand} '
                         f'- {second_operand}\nYour answer: ')
    if int(user_answer) == right_answer:
        print("Correct!")
    else:
        exit(f"'{user_answer}' is wrong answer ;(."
             f"Correct answer was '{right_answer}'."
             f" Let's try again, {name_user}!")


def multiply_func(first_operand, second_operand, name_user):
    right_answer = first_operand * second_operand
    user_answer = string(f'Question: {first_operand} '
                         f'* {second_operand}\nYour answer: ')
    if int(user_answer) == right_answer:
        print("Correct!")
    else:
        exit(f"'{user_answer}' is wrong answer ;(."
             f"Correct answer was '{right_answer}'."
             f" Let's try again, {name_user}!")


def sort_func(focus_operator, name_user):
    first_operand = randint(10, 50)
    second_operand = randint(0, 10)
    if focus_operator == '+':
        sum_func(first_operand, second_operand, name_user)
    elif focus_operator == '-':
        subtract_func(first_operand, second_operand, name_user)
    elif focus_operator == '*':
        multiply_func(first_operand, second_operand, name_user)


def calc(name_user):
    print('What is the result of the expression?')
    count = 0
    operators = ["+", "-", "*"]
    while count < 3:
        focus_operator = operators[randint(0, 2)]
        sort_func(focus_operator, name_user)
        count += 1
    print(f'Congratulations, {name_user}!')
