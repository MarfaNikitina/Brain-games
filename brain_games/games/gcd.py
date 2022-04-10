#!/usr/bin/env python3
from random import randint
import math


def gcd():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    ran_expression = '{} {}'.format(num1, num2)
    true_result = str(math.gcd(num1, num2))
    return ran_expression, true_result


(expression, true_answer) = gcd()
RULE_OF_THE_GAME = 'Find the greatest common divisor of given numbers.'
