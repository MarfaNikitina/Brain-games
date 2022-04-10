#!/usr/bin/env python3
from brain_games.games import even
from brain_games.games.common import common_logic_of_games


(expression, true_answer) = even()
RULE_OF_THE_GAME = 'Answer "yes" if the number is even,' \
                       ' otherwise answer "no".'


def main():
    common_logic_of_games(expression, true_answer, RULE_OF_THE_GAME)


if __name__ == '__main__':
    main()
