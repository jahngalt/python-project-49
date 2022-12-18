#!/usr/bin/env python3
from brain_games.game_core import welcome_user
from brain_games.game_core import game_core


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    game_core(name)


if __name__ == '__main__':
    main()