#!/usr/bin/env python3
from brain_games.games import prime
from brain_games.common_logic import common_logic_of_games


def main():
    common_logic_of_games(prime.expression,
                          prime.true_answer,
                          prime.RULE_OF_THE_GAME)


if __name__ == '__main__':
    main()
