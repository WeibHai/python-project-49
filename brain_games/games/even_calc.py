from random import randint
import prompt


def main():
    count = 0

    while count < 3:
        operators = ["+", "-", "*"]
        focus_operator = operators[randint(0, 2)]
        if focus_operator == "+":
            first_operand = randint(10, 20)
            second_operand = randint(0, 10)
            right_answer = first_operand + second_operand
            answer = prompt.string(f'Question: {first_operand} '
                                   f'+ {second_operand}\nYour answer: ')
            if int(answer) == right_answer:
                print("Correct!")
                count += 1
            else:
                print(f"'{answer}' is wrong answer ;(."
                      f"Correct answer was '{right_answer}'."
                      f" Let's try again, {name_user}!")
                break

        elif focus_operator == "-":
            first_operand = randint(10, 20)
            second_operand = randint(0, 10)
            right_answer = first_operand - second_operand
            answer = prompt.string(f'Question: {first_operand} '
                                   f'- {second_operand}\nYour answer: ')
            if int(answer) == right_answer:
                print("Correct!")
                count += 1
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was '{right_answer}'."
                      f" Let's try again, {name_user}!")
                break

        elif focus_operator == "*":
            first_operand = randint(10, 20)
            second_operand = randint(0, 10)
            right_answer = first_operand * second_operand
            answer = prompt.string(f'Question:" {first_operand} '
                                   f'* {second_operand}\nYour answer: ')
            if int(answer) == right_answer:
                print("Correct!")
                count += 1
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was '{right_answer}'."
                      f" Let's try again, {name_user}!")
                break
    if count == 3:
        print(f'Congratulations, {name_user}!')

if __name__ == "__main__":
    main()
    
