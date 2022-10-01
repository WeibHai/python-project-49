from brain_games.even_parity_check import first_qst
from brain_games.even_greeting import welcome_user


def main():
    name_user = welcome_user()
    first_qst(name_user)


if __name__ == "__main__":
    main()
