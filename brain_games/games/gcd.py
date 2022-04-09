#!/usr/bin/env python3
from random import randint
import math


def gcd():
    rule_of_the_game = 'Find the greatest common divisor of given numbers.'
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    expression = '{} {}'.format(num1, num2)
    true_answer = str(math.gcd(num1, num2))
    return (expression, true_answer, rule_of_the_game)
