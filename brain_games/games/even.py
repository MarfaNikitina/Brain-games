#!/usr/bin/env python3
from random import randint


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def even():
    random_number = randint(1, 100)
    if is_even(random_number):
        true_result = 'yes'
    else:
        true_result = 'no'
    return random_number, true_result


(expression, true_answer) = even()
RULE_OF_THE_GAME = 'Answer "yes" if the number is even,' \
                       ' otherwise answer "no".'
