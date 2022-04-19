#!/usr/bin/env python3
from random import randint, choice
import operator
RULE = 'What is the result of the expression?'


def generate_question_and_answer():
    numb1 = randint(1, 100)
    numb2 = randint(1, 100)
    operators = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul}
    random_operator = choice(list(operators.keys()))
    correct_operator = operators[random_operator]
    correct_answer = str(correct_operator(numb1, numb2))
    question = str(numb1) + ' ' + random_ops + ' ' + str(numb2)
    return question, correct_answer
