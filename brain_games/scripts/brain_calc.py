#!/usr/bin/env python3
from brain_games.games.even_greeting import welcome_user
from brain_games.distributor import distribution_func


def main():
    name_user = welcome_user()
    print('What is the result of the expression?')
    distribution_func("calc", name_user)


if __name__ == '__main__':
    main()
