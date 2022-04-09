#!/usr/bin/env python3
from random import randint


def even():
    expression = randint(1, 100)
    rule_of_the_game = 'Answer "yes" if the number is even, otherwise answer "no".'
    if expression % 2 == 0:
        true_answer = 'yes'
    else:
        true_answer = 'no'
    return expression, true_answer, rule_of_the_game
