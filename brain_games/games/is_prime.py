#!/usr/bin/env python3
from random import randint


def is_prime(num):
    dev = 2
    while num % dev != 0:
        dev += 1
    return dev == num


def prime():
    ran_expression = randint(1, 100)
    if is_prime(ran_expression):
        true_result = 'yes'
    else:
        true_result = 'no'
    return ran_expression, true_result


(expression, true_answer) = prime()
RULE_OF_THE_GAME = 'Answer "yes" if given number is prime.' \
                       ' Otherwise answer "no".'
