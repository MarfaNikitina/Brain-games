#!/usr/bin/env python3
from random import randint, choice


def make_progression():
    num = randint(0, 10)
    step = randint(1, 10)
    progr_list = []
    for i in range(10):
        next_step = num + step * i
        progr_list.append(next_step)
    return progr_list


def progression():
    RULE_OF_THE_GAME = 'What number is missing in the progression?'
    random_expression = make_progression()
    secret_num = choice(random_expression)
    true_answer = str(secret_num)
    expression = ''
    for numb in random_expression:
        if numb == secret_num:
            expression = expression + ' ' + '..'
        else:
            expression = expression + ' ' + str(numb)
    return (expression, true_answer, RULE_OF_THE_GAME)
