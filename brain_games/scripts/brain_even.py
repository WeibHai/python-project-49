from brain_games.games.even_parity_check import first_qst
from brain_games.games.even_greeting import welcome_user
from brain_games.games.even_calc import calc


def main():
    name_user = welcome_user()
    first_qst(name_user)
    calc(name_user)


if __name__ == "__main__":
    main()
