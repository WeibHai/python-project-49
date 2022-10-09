from prompt import string
from brain_games.games import calculator
from brain_games.games import even
from brain_games.games import gcd
from brain_games.games import prime
from brain_games.games import progression


def distribution(game):
    print("Welcome to the Brain Games!")

    name_user = string('May I have your name? ')
    print(f'Hello, {name_user}!')
    print(eval(game).answer)
    count = 0
    while count < 3:
        right_answer = eval(game).run_game()
        user_answer = string('Your answer: ')
        if str(user_answer) == str(right_answer):
            print("Correct!")
            count += 1
        else:
            count = 5
    else:
        if count == 3:
            print(f'Congratulations, {name_user}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{right_answer}'."
                  f" Let's try again, {name_user}!")
