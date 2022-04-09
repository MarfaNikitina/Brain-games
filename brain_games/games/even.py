#!/usr/bin/env python3
from random import randint


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def even():
    RULE_OF_THE_GAME = 'Answer "yes" if the number is even,' \
                       ' otherwise answer "no".'
    expression = randint(1, 100)
    if is_even(expression):
        true_answer = 'yes'
    else:
        true_answer = 'no'
    return (expression, true_answer, RULE_OF_THE_GAME)
