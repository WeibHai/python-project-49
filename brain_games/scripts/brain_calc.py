from brain_games.games.even_greeting import welcome_user
from brain_games.games.calculator_games import calc


def main():
    name_user = welcome_user()
    calc(name_user)


if __name__ == '__main__':
    main()
