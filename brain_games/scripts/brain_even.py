#!/usr/bin/env python3
from brain_games.games import even
from brain_games.common_logic import start_the_game


def main():
    start_the_game(even.game)


if __name__ == '__main__':
    main()
