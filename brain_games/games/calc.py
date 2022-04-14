#!/usr/bin/env python3
from random import randint, choice
import operator
RULE_OF_THE_GAME = 'What is the result of the expression?'


def game():
    numb1 = randint(1, 100)
    numb2 = randint(1, 100)
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul}
    random_ops = choice(list(ops.keys()))
    correct_operator = ops[random_ops]
    correct_answer = correct_operator(numb1, numb2)
    question = str(numb1) + ' ' + random_ops + ' ' + str(numb2)
    return question, correct_answer
