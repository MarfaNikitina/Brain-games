#!/usr/bin/env python3
from random import randint
import math
RULE = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = '{} {}'.format(num1, num2)
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer
