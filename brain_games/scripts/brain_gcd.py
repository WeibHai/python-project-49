from brain_games.games.even_greeting import welcome_user
from brain_games.games.gcd_games import gcd


def main():
    name_user = welcome_user()
    gcd(name_user)


if __name__ == '__main__':
    main()
