#!/usr/bin/env python3
from brain_games.games import calc
from brain_games.common_logic import common_logic_of_games


def main():
    common_logic_of_games(calc.game)


if __name__ == '__main__':
    main()
