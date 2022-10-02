from brain_games.games.even_greeting import welcome_user
from brain_games.games.even_calc import run_calc


def main():
    name_user = welcome_user()
    run_calc(name_user)


if __name__ == '__main__':
    main()
