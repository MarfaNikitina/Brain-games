#!/usr/bin/env python3
from random import randint


def is_prime(num):
    devider = 2
    while num % devider != 0:
        devider += 1
    return devider == num


def prime():
    RULE_OF_THE_GAME = 'Answer "yes" if given number is prime.' \
                       ' Otherwise answer "no".'
    expression = randint(1, 100)
    if is_prime(expression):
        true_answer = 'yes'
    else:
        true_answer = 'no'
    return (expression, true_answer, RULE_OF_THE_GAME)
