#!/usr/bin/env python3
from brain_games.games.even_games import parity_check
from brain_games.games.even_greeting import welcome_user


def main():
    name_user = welcome_user()
    parity_check(name_user)


if __name__ == "__main__":
    main()
