#!/usr/bin/env python3
from brain_games.games import even
from brain_games.games.common import common_logic_of_games


def main():
    common_logic_of_games(even.expression, even.true_answer, even.RULE_OF_THE_GAME)


if __name__ == '__main__':
    main()
