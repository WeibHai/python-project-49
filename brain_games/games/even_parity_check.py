import prompt


def third_qst(name_user):
    second_answer = prompt.string('Question: 7\nYour answer: ')
    if second_answer == "no":
        print(f'Congratulations, {name_user}!')
    else:
        print((f"yes' is wrong answer ;(."
               f"Correct answer was 'no'.\nLet's try again, {name_user}!"))


def second_qst(name_user):
    second_answer = prompt.string('Question: 6\nYour answer: ')
    if second_answer == "yes":
        print('Correct!')
        third_qst(name_user)
    else:
        print((f"no' is wrong answer ;(."
               f"Correct answer was 'yes'.\nLet's try again, {name_user}!"))


def first_qst(name_user):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    first_answer = prompt.string('Question: 15\nYour answer: ')
    if first_answer == "no":
        print('Correct!')
        second_qst(name_user)
    else:
        print((f"yes' is wrong answer ;(."
               f"Correct answer was 'no'.\nLet's try again, {name_user}!"))
