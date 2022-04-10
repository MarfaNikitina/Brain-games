#!/usr/bin/env python3
from random import randint, choice


def make_progression():
    num = randint(0, 10)
    step = randint(1, 10)
    progression_list = []
    for i in range(10):
        next_step = num + step * i
        progression_list.append(next_step)
    return progression_list


def progression():
    random_expression = make_progression()
    secret_num = choice(random_expression)
    true_result = str(secret_num)
    visible_expression = ''
    for numb in random_expression:
        if numb == secret_num:
            visible_expression = visible_expression + ' ' + '..'
        else:
            visible_expression = visible_expression + ' ' + str(numb)
    return visible_expression, true_result


RULE_OF_THE_GAME = 'What number is missing in the progression?'
(expression, true_answer) = progression()
