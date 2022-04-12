#!/usr/bin/env python3
from random import randint
import math


def game():
    RULE_OF_THE_GAME = 'Find the greatest common divisor of given numbers.'
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = '{} {}'.format(num1, num2)
    true_result = str(math.gcd(num1, num2))
    return question, true_result, RULE_OF_THE_GAME
