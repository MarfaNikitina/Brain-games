#!/usr/bin/env python3
from random import randint


RULE_OF_THE_GAME = 'Answer "yes" if given number is prime.' \
                   'Otherwise answer "no".'


def is_prime(num):
    dev = 2
    while num % dev != 0:
        dev += 1
    return dev == num


def game():
    question = randint(1, 100)
    if is_prime(question):
        true_result = 'yes'
    else:
        true_result = 'no'
    return question, true_result
