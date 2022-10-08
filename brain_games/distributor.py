from brain_games.games.calculator_games import calc
from brain_games.games.gcd_games import gcd
from brain_games.games.prime_games import prime
from brain_games.games.progression_games import progression
from brain_games.games.even_games import parity_check


def print_result(answer_func, right_answer, user_answer, name_user):
    if answer_func == 'yes':
        print(f'Congratulations, {name_user}!')
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f"Correct answer was '{right_answer}'."
              f" Let's try again, {name_user}!")


def exit_func(count, right_answer, user_answer, name_user):
    if count == 3:
        print_result("yes", right_answer, user_answer, name_user)
    else:
        print_result("no", right_answer, user_answer, name_user)


def func_right_or_wrong(right_answer, user_answer):
    if str(user_answer) == str(right_answer):
        return 1
    else:
        return 0


def sort_func(games):
    if games == 'calc':
        answer_func = calc()
        return answer_func
    elif games == 'gcd':
        answer_func = gcd()
        return answer_func
    elif games == 'prime':
        answer_func = prime()
        return answer_func
    elif games == 'progression':
        answer_func = progression()
        return answer_func
    else:
        answer_func = parity_check()
        return answer_func


def distribution_func(games, name_user):
    count = 0
    while count < 3:
        list_answers = sort_func(games)
        right_answer = list_answers[0]
        user_answer = list_answers[1]
        if func_right_or_wrong(right_answer, user_answer) == 1:
            count += 1
            print("Correct!")
        else:
            count = 25
    else:
        exit_func(count, right_answer, user_answer, name_user)
