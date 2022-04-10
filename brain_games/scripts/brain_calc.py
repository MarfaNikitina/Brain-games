#!/usr/bin/env python3
from brain_games.games import calc
from brain_games.games.common import common_logic_of_games


def main():
    common_logic_of_games(calc.expression, calc.true_answer, calc.RULE_OF_THE_GAME)


if __name__ == '__main__':
    main()
