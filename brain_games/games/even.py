#!/usr/bin/env python3
from random import randint


RULE_OF_THE_GAME = 'Answer "yes" if the number is even, ' \
                   'otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def game():
    question = randint(1, 100)
    if is_even(random_number):
        true_result = 'yes'
    else:
        true_result = 'no'
    return question, true_result
