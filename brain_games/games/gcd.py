#!/usr/bin/env python3
from random import randint
import math


def gcd():
    RULE_OF_THE_GAME = 'Find the greatest common divisor of given numbers.'
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    expression = '{} {}'.format(num1, num2)
    true_answer = str(math.gcd(num1, num2))
    result_touple = (expression, true_answer, RULE_OF_THE_GAME)
    return result_touple
