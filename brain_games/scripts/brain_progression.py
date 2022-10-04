from brain_games.games.even_greeting import welcome_user
from brain_games.games.even_progression import form_func


def main():
    name_user = welcome_user()
    form_func(name_user)


if __name__ == '__main__':
    main()
