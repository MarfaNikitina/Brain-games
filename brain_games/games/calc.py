#!/usr/bin/env python3
import prompt
from random import randint, choice
import operator


def create_random_expr():
    numb1 = randint(1, 100)
    numb2 = randint(1, 100)
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul}
    random_ops = choice(list(ops.keys()))
    ran_expression = str(numb1) + random_ops + str(numb2)
    return ran_expression


def calc():
    rule_of_the_game = 'What is the result of the expression?'
    expression = create_random_expr()
    true_answer = str(eval(ran_expression))
    return (expression, true_answer, rule_of_the_game)