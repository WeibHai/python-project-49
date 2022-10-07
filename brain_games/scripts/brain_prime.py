#!/usr/bin/env python3
from brain_games.games.even_greeting import welcome_user
from brain_games.games.prime_games import prime


def main():
    name_user = welcome_user()
    prime(name_user)


if __name__ == '__main__':
    main()
