#!/usr/bin/env python3
from brain_games.games import gcd
from brain_games.common_logic import common_logic_of_games


def main():
    common_logic_of_games(gcd.expression,
                          gcd.true_answer,
                          gcd.RULE_OF_THE_GAME)


if __name__ == '__main__':
    main()
