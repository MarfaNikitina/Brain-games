#!/usr/bin/env python3
from random import randint
RULE_OF_THE_GAME = 'Answer "yes" if given number is prime.' \
                       'Otherwise answer "no".'


def is_prime(num):
    devider = 2
    while num % devider != 0:
        devider += 1
    return devider == num


def game():
    question = randint(1, 100)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
