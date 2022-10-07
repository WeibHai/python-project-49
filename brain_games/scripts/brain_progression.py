#!/usr/bin/env python3
from brain_games.games.even_greeting import welcome_user
from brain_games.games.progression_games import progression


def main():
    name_user = welcome_user()
    progression(name_user)


if __name__ == '__main__':
    main()
