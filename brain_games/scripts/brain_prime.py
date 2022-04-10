#!/usr/bin/env python3
from brain_games.games import is_prime
from brain_games.games.common import common_logic_of_games


def main():
    common_logic_of_games(is_prime.expression, is_prime.true_answer, is_prime.RULE_OF_THE_GAME)


if __name__ == '__main__':
    main()
