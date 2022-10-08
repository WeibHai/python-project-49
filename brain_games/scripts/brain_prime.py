#!/usr/bin/env python3
from brain_games.games.even_greeting import welcome_user
from brain_games.distributor import distribution_func


def main():
    name_user = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    distribution_func("prime", name_user)


if __name__ == '__main__':
    main()
