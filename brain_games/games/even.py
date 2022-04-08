#!/usr/bin/env python3
import prompt
from random import randint


def is_even(number):
    """функция считает число четное или нет"""
    if number % 2 == 0:
        return True
    else:
        return False


def even():
    expression = randint(1, 100)
    rule_of_the_game = 'Answer "yes" if the number is even, otherwise answer "no".'
    if is_even(expression):
        true_answer = 'yes'
    else:
        true_answer = 'no'
    res_tuple = (expression, true_answer, rule_of_the_game)
    return res_tuple
