#!/usr/bin/env python3
from random import randint, choice
import operator


def create_random_expression():
    numb1 = randint(1, 100)
    numb2 = randint(1, 100)
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul}
    random_ops = choice(list(ops.keys()))
    ran_expression = str(numb1) + random_ops + str(numb2)
    return ran_expression


def calc():
    RULE_OF_THE_GAME = 'What is the result of the expression?'
    expression = create_random_expression()
    true_answer = str(eval(expression))
    return (expression, true_answer, RULE_OF_THE_GAME)
