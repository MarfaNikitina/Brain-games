#!/usr/bin/env python3
import prompt
from random import randint

def is_prime(num):
    devider = 2
    while num % devider != 0:
        devider += 1
    return devider == num

def prime():
    rule_of_the_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    expression = randint(1, 100)
    if is_prime(expression):
            true_answer = 'yes'
    else:
            true_answer = 'no'
    return (expression, true_answer, rule_of_the_game)
